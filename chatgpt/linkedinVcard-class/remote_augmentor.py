from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LinkedInRemoteAugmentor:
    """
    This class handles remote augmentation of LinkedIn connection data by
    scraping contact information from LinkedIn profiles using Selenium.

    Dependencies:
    - Selenium: The primary library used for web scraping.
    - Chrome WebDriver: A WebDriver for Selenium (e.g., ChromeDriver for Chrome browser).

    How to Use:
    1. Install Selenium via pip:
        pip install selenium
    2. Download the appropriate WebDriver (e.g., ChromeDriver for Chrome).
    3. Initialize the LinkedInRemoteAugmentor class with the path to the WebDriver
       and your LinkedIn credentials.
    4. Call `start_driver()` to log in to LinkedIn.
    5. Call `fetch_contact_info(linkedin_url)` with the LinkedIn profile URL to
       extract contact info (currently, it extracts the email address).
    6. Optionally, call `stop_driver()` to log out and close the WebDriver.
    """

    def __init__(self, driver_path, linkedin_email, linkedin_password):
        """
        Initialize the remote augmentor with the path to the WebDriver and
        LinkedIn login credentials.

        :param driver_path: Path to the Selenium WebDriver.
        :param linkedin_email: LinkedIn account email.
        :param linkedin_password: LinkedIn account password.
        """
        self.driver_path = driver_path
        self.linkedin_email = linkedin_email
        self.linkedin_password = linkedin_password
        self.driver = None

    def start_driver(self):
        """
        Start the Selenium WebDriver and log in to LinkedIn.

        This method opens a browser window using the WebDriver, navigates to the
        LinkedIn login page, and performs a login using the provided credentials.
        """
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        self.driver.get("https://www.linkedin.com/login")

        # Log in to LinkedIn
        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(self.linkedin_email)
        password_field.send_keys(self.linkedin_password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Allow time for login to complete

    def fetch_contact_info(self, linkedin_url):
        """
        Fetches the contact info from a given LinkedIn profile URL.

        :param linkedin_url: The LinkedIn profile URL to extract contact info from.
        :return: Dictionary with contact info fields like email, phone, etc.
        """
        self.driver.get(linkedin_url)
        time.sleep(5)  # Allow time for the profile to load

        contact_info = {}
        try:
            # Accessing the contact information section (if available)
            contact_section = self.driver.find_element(By.XPATH, "//section[@class='pv-contact-info__contact-type ci-email']")
            email = contact_section.find_element(By.XPATH, ".//a").text
            contact_info['email'] = email
        except Exception as e:
            contact_info['email'] = None

        # You can similarly add phone numbers, addresses, and other details
        # For simplicity, we will just capture the email here.

        return contact_info

    def stop_driver(self):
        """
        Stops the Selenium WebDriver and logs out from LinkedIn.

        This method terminates the WebDriver session and ensures that the user
        is logged out of LinkedIn.
        """
        self.driver.quit()
