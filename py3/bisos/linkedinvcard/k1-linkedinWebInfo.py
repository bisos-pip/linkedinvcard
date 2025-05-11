import time
import logging
from pathlib import Path
from typing import Optional, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


import urllib.parse



logger = logging.getLogger(__name__)

class LinkedInRemoteAugmentor:
    """
    Automates LinkedIn profile contact info extraction using an existing Chrome login session.

    Requirements:
    - User must be already logged into LinkedIn in Chrome.
    - Chrome must be closed before starting this script (profile cannot be in use).
    """

    def __init__(self, chrome_user_data_dir: Path, chrome_profile: str = "Default"):
        """
        Initialize with path to Chrome user data and profile.

        :param chrome_user_data_dir: Base directory for Chrome user data (e.g., ~/.config/google-chrome)
        :param chrome_profile: Profile name within Chrome (e.g., 'Default', 'Profile 1')
        """
        self.chrome_user_data_dir = chrome_user_data_dir
        self.chrome_profile = chrome_profile
        self.driver: Optional[webdriver.Chrome] = None

    def start_driverExisting(self) -> None:
        """
        Start Chrome WebDriver using existing profile for logged-in session reuse.
        """
        logger.info("Launching Chrome with profile reuse...")

        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={self.chrome_user_data_dir}")
        options.add_argument(f"--profile-directory={self.chrome_profile}")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        logger.info("Chrome WebDriver started.")
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(3)


    def start_driverLogin(self, username, password):
        """
        Start the Selenium WebDriver and log in to LinkedIn.

        This method opens a browser window using the WebDriver, navigates to the
        LinkedIn login page, and performs a login using the provided credentials.
        """

        logger.info("Launching Chrome with profile reuse...")

        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={self.chrome_user_data_dir}")
        options.add_argument(f"--profile-directory={self.chrome_profile}")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        logger.info("Chrome WebDriver started.")

        self.driver.get("https://www.linkedin.com/login")

        # Log in to LinkedIn
        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Allow time for login to complete

    def fetch_contact_info(self, linkedin_url: str) -> Dict[str, Optional[str]]:
        """
        Extract contact info (email and profile URL) from a LinkedIn profile's contact-info overlay.
        """
        if not self.driver:
            raise RuntimeError("WebDriver is not started. Call start_driver() first.")

        logger.info(f"Visiting LinkedIn profile: {linkedin_url}")
        self.driver.get(linkedin_url)
        time.sleep(3)

        contact_info = {"email": None, "profile_url": None}

        try:
            contact_info_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "top-card-text-details-contact-info"))
            )
            contact_info_button.click()
            logger.debug("Clicked on contact info button.")
            time.sleep(2)  # give modal time to load
        except Exception as e:
            logger.warning(f"Could not click contact info button: {e}")
            return contact_info

        # Use visible text to locate email and profile URL
        try:
            email_elem = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href, 'mailto:')]"))
            )
            contact_info['email'] = email_elem.text.strip()
            logger.debug(f"Found email: {contact_info['email']}")
        except Exception:
            logger.info("Email not found.")

        try:
            profile_elem = self.driver.find_element(
                By.XPATH, "//a[contains(@href, 'linkedin.com/in/')]"
            )
            contact_info['profile_url'] = profile_elem.get_attribute("href")
            logger.debug(f"Found profile URL: {contact_info['profile_url']}")
        except Exception:
            logger.info("Profile URL not found.")

        return contact_info


    def fetch_contact_infoDebug(self, linkedin_url: str) -> Dict[str, Optional[str]]:
        """
        Extract contact info (email and profile URL) from a LinkedIn profile's contact-info overlay.

        :param linkedin_url: Public LinkedIn profile URL.
        :return: Dict with contact info, including 'email' and 'profile_url'.
        """
        if not self.driver:
            raise RuntimeError("WebDriver is not started. Call start_driver() first.")

        logger.info(f"Visiting LinkedIn profile: {linkedin_url}")
        self.driver.get(linkedin_url)
        time.sleep(3)  # Let main profile page settle

        contact_info: Dict[str, Optional[str]] = {"email": None, "profile_url": None}

        # Click the Contact Info button (using known ID)
        try:
            contact_info_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "top-card-text-details-contact-info"))
            )
            contact_info_button.click()
            logger.debug("Clicked on contact info button.")
            logger.debug("Capture the HTML after clicking")
            html = self.driver.page_source
            with open("/tmp/linkedin_modal_debug.html", "w") as f:
                f.write(html)
        except Exception as e:
            logger.warning(f"Could not click contact info button: {e}")
            return contact_info

        # Wait for the overlay modal to appear
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pv-contact-info"))
            )
            logger.debug("Contact info modal is visible.")

            try:
                email_elem = self.driver.find_element(
                    By.XPATH, "//section[h3[contains(text(), 'Email')]]//a[starts-with(@href, 'mailto:')]"
                )
                contact_info['email'] = email_elem.text.strip()
            except NoSuchElementException:
                logger.info("Email not found in modal.")

            try:
                profile_elem = self.driver.find_element(
                    By.XPATH, "//section[h3[contains(text(), 'Your Profile')]]//a[contains(@href, 'linkedin.com/in/')]"
                )
                contact_info['profile_url'] = profile_elem.get_attribute("href")
            except NoSuchElementException:
                logger.info("Profile URL not found in modal.")

        except Exception as e:
            logger.warning(f"Contact info modal did not load: {e}")

        return contact_info


        # # Construct the overlay URL
        # parsed_url = urllib.parse.urlparse(linkedin_url)
        # path_parts = parsed_url.path.rstrip('/').split('/')
        # if len(path_parts) < 2 or path_parts[1] != 'in':
        #     logger.warning(f"Unexpected LinkedIn profile URL format: {linkedin_url}")
        #     return contact_info

        # overlay_url = f"https://www.linkedin.com/in/{path_parts[2]}/overlay/contact-info"
        # logger.info(f"Visiting contact info overlay: {overlay_url}")
        # self.driver.get(overlay_url)

        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "pv-contact-info__contact-type"))
        #     )
        #     logger.debug("Contact info overlay loaded.")

        #     # Extract email
        #     try:
        #         email_elem = self.driver.find_element(
        #             By.XPATH, "//section[h3[contains(text(), 'Email')]]//a[starts-with(@href, 'mailto:')]"
        #         )
        #         contact_info['email'] = email_elem.text.strip()
        #         logger.info(f"Email found: {contact_info['email']}")
        #     except NoSuchElementException:
        #         logger.info("Email not found.")

        #     # Extract profile URL
        #     try:
        #         profile_elem = self.driver.find_element(
        #             By.XPATH, "//section[h3[contains(text(), 'Your Profile')]]//a[contains(@href, 'linkedin.com/in/')]"
        #         )
        #         contact_info['profile_url'] = profile_elem.get_attribute("href")
        #         logger.info(f"Profile URL found: {contact_info['profile_url']}")
        #     except NoSuchElementException:
        #         logger.info("Profile URL not found.")

        # except (TimeoutException, NoSuchElementException) as e:
        #     logger.warning(f"Failed to extract contact info from: {linkedin_url} — {e}")

        return contact_info



    def fetch_contact_infoClose(self, linkedin_url: str) -> Dict[str, Optional[str]]:
        """
        Extract contact info (email) from a LinkedIn profile using the contact-info overlay.

        :param linkedin_url: Public LinkedIn profile URL.
        :return: Dict with contact info (currently only 'email').
        """
        if not self.driver:
            raise RuntimeError("WebDriver is not started. Call start_driver() first.")

        logger.info(f"Visiting LinkedIn profile: {linkedin_url}")
        self.driver.get(linkedin_url)
        time.sleep(3)  # Let main profile page settle

        contact_info: Dict[str, Optional[str]] = {"email": None}

        # Construct the overlay URL
        parsed_url = urllib.parse.urlparse(linkedin_url)
        path_parts = parsed_url.path.rstrip('/').split('/')
        if len(path_parts) < 2 or path_parts[1] != 'in':
            logger.warning(f"Unexpected LinkedIn profile URL format: {linkedin_url}")
            return contact_info

        overlay_url = f"https://www.linkedin.com/in/{path_parts[2]}/overlay/contact-info"
        logger.info(f"Visiting contact info overlay: {overlay_url}")
        self.driver.get(overlay_url)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pv-contact-info"))
            )
            logger.debug("Contact info overlay loaded.")

            email_elem = self.driver.find_element(
                By.XPATH, "//section[contains(@class, 'ci-email')]//a"
            )
            contact_info['email'] = email_elem.text.strip()
            logger.info(f"Email found: {contact_info['email']}")

        except (TimeoutException, NoSuchElementException) as e:
            logger.warning(f"No email found on profile: {linkedin_url} — {e}")

        return contact_info


    def fetch_contact_infoBAD(self, linkedin_url: str) -> Dict[str, Optional[str]]:
        """
        Extract contact info (email) from a LinkedIn profile.

        :param linkedin_url: Public LinkedIn profile URL.
        :return: Dict with contact info (currently only 'email').
        """
        if not self.driver:
            raise RuntimeError("WebDriver is not started. Call start_driver() first.")

        logger.info(f"Visiting LinkedIn profile: {linkedin_url}")
        self.driver.get(linkedin_url)
        time.sleep(5)  # Wait for page to load

        contact_info: Dict[str, Optional[str]] = {"email": None}

        try:
            # Click the "Contact Info" button
            contact_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-control-name='contact_see_more']"))
            )
            contact_button.click()
            logger.debug("Clicked contact info button.")

            # Wait for the modal to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pv-contact-info"))
            )
            logger.debug("Contact info modal appeared.")

            # Extract the email from the modal
            email_elem = self.driver.find_element(
                By.XPATH, "//section[contains(@class, 'ci-email')]//a"
            )
            contact_info['email'] = email_elem.text.strip()
            logger.info(f"Email found: {contact_info['email']}")

        except (TimeoutException, NoSuchElementException) as e:
            logger.warning(f"No email found on profile: {linkedin_url} — {e}")

        return contact_info


    def fetch_contact_infoOld(self, linkedin_url: str) -> Dict[str, Optional[str]]:
        """
        Extract contact info (email) from a LinkedIn profile.

        :param linkedin_url: Public LinkedIn profile URL.
        :return: Dict with contact info (currently only 'email').
        """
        if not self.driver:
            raise RuntimeError("WebDriver is not started. Call start_driver() first.")

        logger.info(f"Visiting LinkedIn profile: {linkedin_url}")
        self.driver.get(linkedin_url)
        time.sleep(5)

        contact_info: Dict[str, Optional[str]] = {}

        try:
            contact_section = self.driver.find_element(
                By.XPATH,
                "//section[contains(@class,'pv-contact-info__contact-type') and contains(@class,'ci-email')]"
            )
            email_elem = contact_section.find_element(By.XPATH, ".//a")
            contact_info['email'] = email_elem.text.strip()
            logger.info(f"Email found: {contact_info['email']}")
        except Exception as e:
            logger.warning(f"No email found on profile: {linkedin_url} — {e}")
            contact_info['email'] = None

        return contact_info

    def stop_driver(self) -> None:
        """
        Stop the Chrome WebDriver and close browser.
        """
        if self.driver:
            logger.info("Closing Chrome WebDriver.")
            self.driver.quit()
            self.driver = None



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# class LinkedInRemoteAugmentor:
#     """
#     This class handles remote augmentation of LinkedIn connection data by
#     scraping contact information from LinkedIn profiles using Selenium.

#     Dependencies:
#     - Selenium: The primary library used for web scraping.
#     - Chrome WebDriver: A WebDriver for Selenium (e.g., ChromeDriver for Chrome browser).

#     How to Use:
#     1. Install Selenium via pip:
#         pip install selenium
#     2. Download the appropriate WebDriver (e.g., ChromeDriver for Chrome).
#     3. Initialize the LinkedInRemoteAugmentor class with the path to the WebDriver
#        and your LinkedIn credentials.
#     4. Call `start_driver()` to log in to LinkedIn.
#     5. Call `fetch_contact_info(linkedin_url)` with the LinkedIn profile URL to
#        extract contact info (currently, it extracts the email address).
#     6. Optionally, call `stop_driver()` to log out and close the WebDriver.
#     """

#     def __init__(self, driver_path, linkedin_email, linkedin_password):
#         """
#         Initialize the remote augmentor with the path to the WebDriver and
#         LinkedIn login credentials.

#         :param driver_path: Path to the Selenium WebDriver.
#         :param linkedin_email: LinkedIn account email.
#         :param linkedin_password: LinkedIn account password.
#         """
#         self.driver_path = driver_path
#         self.linkedin_email = linkedin_email
#         self.linkedin_password = linkedin_password
#         self.driver = None

#     def start_driver(self):
#         """
#         Start the Selenium WebDriver and log in to LinkedIn.

#         This method opens a browser window using the WebDriver, navigates to the
#         LinkedIn login page, and performs a login using the provided credentials.
#         """
#         options = webdriver.ChromeOptions()
#         self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
#         self.driver.get("https://www.linkedin.com/login")

#         # Log in to LinkedIn
#         email_field = self.driver.find_element(By.ID, "username")
#         password_field = self.driver.find_element(By.ID, "password")
#         email_field.send_keys(self.linkedin_email)
#         password_field.send_keys(self.linkedin_password)
#         password_field.send_keys(Keys.RETURN)
#         time.sleep(5)  # Allow time for login to complete

#     def fetch_contact_info(self, linkedin_url):
#         """
#         Fetches the contact info from a given LinkedIn profile URL.

#         :param linkedin_url: The LinkedIn profile URL to extract contact info from.
#         :return: Dictionary with contact info fields like email, phone, etc.
#         """
#         self.driver.get(linkedin_url)
#         time.sleep(5)  # Allow time for the profile to load

#         contact_info = {}
#         try:
#             # Accessing the contact information section (if available)
#             contact_section = self.driver.find_element(By.XPATH, "//section[@class='pv-contact-info__contact-type ci-email']")
#             email = contact_section.find_element(By.XPATH, ".//a").text
#             contact_info['email'] = email
#         except Exception as e:
#             contact_info['email'] = None

#         # You can similarly add phone numbers, addresses, and other details
#         # For simplicity, we will just capture the email here.

#         return contact_info

#     def stop_driver(self):
#         """
#         Stops the Selenium WebDriver and logs out from LinkedIn.

#         This method terminates the WebDriver session and ensures that the user
#         is logged out of LinkedIn.
#         """
#         self.driver.quit()
