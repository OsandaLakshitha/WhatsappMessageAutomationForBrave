
# WhatsApp Auto Messaging Bot

A Python script that automatically sends messages to multiple WhatsApp numbers using Brave Browser and Selenium WebDriver.

It reads phone numbers from an Excel file (contacts.xlsx) and sends a customizable message to each number, waiting until the message is delivered before moving on.

---

## Features

- ✅ Send WhatsApp messages to multiple contacts from an Excel file.
- ✅ Supports Brave browser (Chromium-based).
- ✅ Automatically waits until the message is delivered (double gray ticks).
- ✅ Works with both Sri Lankan and UK phone numbers (or any country).
- ✅ Handles invalid numbers and errors gracefully.

---

## Requirements

- Python 3.10+
- Brave Browser installed on your machine
- ChromeDriver matching your Brave version
- Python packages:
  pip install pandas selenium openpyxl

---

## Setup Instructions

1. Clone this repository:
   git clone https://github.com/OsandaLakshitha/WhatsappMessageAutomationForBrave.git
   cd WhatsappMessageAutomationForBrave

2. Download matching ChromeDriver for Brave:
   - Go to: https://googlechromelabs.github.io/chrome-for-testing/
   - Download the version matching your Brave browser version.
   - Place chromedriver.exe in a folder (e.g., C:\drivers\chromedriver.exe).

3. Prepare your Excel file:
   - Ensure contacts.xlsx has a column named 'Phone'.
   - Example:
     | Phone        |
     | ------------ |
     | +94771234567 |
     | +447912345678|

4. Edit the script:
   - Update brave_path to your Brave installation path:
     brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
   - Update driver_path to your ChromeDriver path:
     driver_path = r"C:\drivers\chromedriver.exe"
   - Customize your message in the message variable.

5. Run the script:
   python TextAll.py
   - Scan the QR code in WhatsApp Web when prompted.
   - The script will send messages and wait for delivery before moving to the next contact.

---

## Notes

- Make sure the phone numbers include the country code (+94 for Sri Lanka, +44 for UK, etc.).
- Do not send spam – WhatsApp may block accounts for excessive messages.
- Script is designed for personal or business automation with proper consent.

---

## License

This project is licensed under the MIT License.
