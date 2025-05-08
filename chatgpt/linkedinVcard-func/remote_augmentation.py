import time
import vobject
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver (for Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: run without opening a browser window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to extract contact info from a LinkedIn profile
def extract_contact_info(linkedin_url):
    driver.get(linkedin_url)
    time.sleep(5)  # Wait for page to load

    contact_info = {}

    # Attempt to extract email
    try:
        email_element = driver.find_element(By.XPATH, '//a[contains(@href, "mailto:")]')
        contact_info['EMAIL'] = email_element.get_attribute('href').replace('mailto:', '')
    except Exception as e:
        contact_info['EMAIL'] = 'Not Available'

    # Attempt to extract phone number (this field is not always available)
    try:
        phone_element = driver.find_element(By.XPATH, '//span[contains(text(), "Phone")]')
        contact_info['TEL'] = phone_element.find_element(By.XPATH, '..').text.split(":")[1].strip()
    except Exception as e:
        contact_info['TEL'] = 'Not Available'

    # Extract other information (e.g., Address, Social Media, etc. as needed)
    # You can modify this part to extract additional info based on LinkedIn's layout.

    return contact_info

# Function to load and update vCard with contact info
def update_vcard(vcard_file, contact_info):
    with open(vcard_file, 'r') as f:
        vcard_data = f.read()

    vcard = vobject.readOne(vcard_data)

    # Update the vCard with the extracted contact info
    if 'EMAIL' in contact_info:
        vcard.add('email').value = contact_info['EMAIL']
    if 'TEL' in contact_info:
        vcard.add('tel').value = contact_info['TEL']

    # Add other fields as needed, e.g., address, social media, etc.

    # Save the updated vCard
    updated_vcard_file = vcard_file.replace(".vcf", "_updated.vcf")
    with open(updated_vcard_file, 'w') as f:
        f.write(vcard.serialize())

    print(f"vCard updated and saved to {updated_vcard_file}")

# Main function
def main():
    input_vcard_file = 'path_to_your_vcard.vcf'  # Specify the path to the input vCard
    with open(input_vcard_file, 'r') as f:
        vcard_data = f.read()

    # Parse the LinkedIn URL from the vCard
    vcard = vobject.readOne(vcard_data)
    linkedin_url = vcard.url.value

    if linkedin_url:
        contact_info = extract_contact_info(linkedin_url)
        update_vcard(input_vcard_file, contact_info)
    else:
        print("No LinkedIn URL found in vCard.")

    # Close the browser after processing
    driver.quit()

if __name__ == "__main__":
    main()
