import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

def send_whatsapp_messages(excel_file, message_template):
    # Read phone numbers
    df = pd.read_excel(excel_file)
    phone_numbers = df['Phone'].tolist()

    # Path to Brave browser
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    # Path to matching chromedriver (manually downloaded)
    driver_path = r"C:\drivers\chromedriver.exe"

    # ChromeOptions for Brave
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument("--start-maximized")

    # Initialize driver
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.get("https://web.whatsapp.com")

    print("Please scan the QR code to log in to WhatsApp Web")
    input("Press Enter after you've logged in...")

    for phone in phone_numbers:
        try:
            phone = str(phone).replace(" ", "").replace("-", "").replace("+", "")
            url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote(message_template)}"
            driver.get(url)

            wait = WebDriverWait(driver, 30)
            message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
            
            # Click send button
            send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]')))
            send_button.click()

            # Wait until the message shows "Delivered" (double gray ticks)
            try:
                delivered = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//span[@data-icon="msg-dblcheck"]'))
                )
                print(f"✅ Message delivered to {phone}")
            except:
                print(f"⚠️ Message sent but delivery not confirmed for {phone}")

            time.sleep(2)  # small delay before next message

        except Exception as e:
            print(f"❌ Failed to send message to {phone}: {str(e)}")
            continue

    driver.quit()
    print("🎉 All messages sent!")

if __name__ == "__main__":
    excel_file = "contacts.xlsx"  # must have column 'Phone'
    message = """Hello! 

This is a business message from AmzaumIT.

This is an auto-generated test message.

Thank you!"""

    send_whatsapp_messages(excel_file, message)
