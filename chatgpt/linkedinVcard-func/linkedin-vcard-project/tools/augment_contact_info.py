import argparse
import os
import time
import vobject
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from common_args import add_common_args, validate_common_args

def extract_contact_info(linkedin_url):
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(linkedin_url)
        time.sleep(10)  # Allow manual login/rendering
        contact_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Contact")
        contact_button.click()
        time.sleep(3)
        modal = driver.find_element(By.CLASS_NAME, "artdeco-modal")
        email_elements = modal.find_elements(By.XPATH, "//a[contains(@href, 'mailto:')]")
        emails = [el.get_attribute("href").replace("mailto:", "") for el in email_elements]
        return emails
    finally:
        driver.quit()

def augment_vcard(vcard_path):
    with open(vcard_path, 'r+', encoding='utf-8') as f:
        card = vobject.readOne(f.read())
        url = str(card.url.value)
        emails = extract_contact_info(url)
        for email in emails:
            card.add('email').value = email
        f.seek(0)
        f.write(card.serialize())
        f.truncate()

def main():
    parser = argparse.ArgumentParser(description="Augment vCard with LinkedIn Contact Info.")
    add_common_args(parser)
    args = parser.parse_args()
    validate_common_args(args)

    for filename in os.listdir(args.vcardDir):
        if filename.endswith('.vcf'):
            augment_vcard(os.path.join(args.vcardDir, filename))
            time.sleep(300)  # Wait to avoid triggering LinkedIn rate limits

if __name__ == "__main__":
    main()