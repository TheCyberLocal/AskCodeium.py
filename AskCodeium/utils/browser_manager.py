from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class BrowserManager:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://codeium.com/live/general")
        time.sleep(3)  # Wait for the page to load

    def get_history(self):
        # If popup exists, clear it
        self.clear_popup()

        # Find all div elements on the page
        div_elements = self.driver.find_elements("tag name", "div")

        # Filter out div elements that contain other div elements
        div_texts = [div.text for div in div_elements if not div.find_elements("tag name", "div") and div.text.strip()]

        # Return a list of query/response tuples
        # Div text indexes 3 and 4 are the first query, continue till the last div text
        return [(div_texts[i], div_texts[i+1]) for i in range(3, len(div_texts) - 1, 2)]

    def get_chat(self):
        # If popup exists, clear it
        self.clear_popup()

        # Find all div elements on the page
        div_elements = self.driver.find_elements("tag name", "div")

        # Filter out div elements that contain other div elements
        div_texts = [div.text for div in div_elements if not div.find_elements("tag name", "div") and div.text.strip()]

        # Return the last response div found
        return div_texts[-1]

    def send_chat(self, input_text):
        # If popup exists, clear it
        self.clear_popup()

        # Find the input div
        input_div = self.driver.find_element("css selector", "div.ql-editor")

        # Send the input
        input_div.send_keys(input_text)

        # Wait for the input to be registered
        time.sleep(1)

        input_div.send_keys(Keys.ENTER)

        # Wait for the response to start
        time.sleep(4)

    def clear_chat(self):
        # If popup exists, clear it
        self.clear_popup()

        # Find all button elements on the page
        button_elements = self.driver.find_elements("tag name", "button")

        # Find the clear button
        clear_button = button_elements[-2]

        # Click the clear button
        clear_button.click()

        # Wait for chat to clear
        time.sleep(1)

    def clear_popup(self):
        # Find all button elements on the page
        buttons = self.driver.find_elements("tag name", "button")

        # Define the target class name for closing the popup
        target_class = "font-semibold flex items-center justify-center rounded transition duration-100 ease-in-out focus:outline-none focus:ring-4 bg-brand-dark text-white hover:bg-brand-dark-600 disabled:border-gray-100 disabled:bg-gray-300 focus:ring-primary-700 px-4 py-2 text-base absolute right-6 top-6 h-7 w-7 cursor-pointer"

        # Iterate through all found buttons and click the target button
        for button in buttons:
            if button.get_attribute("class") == target_class:
                # Click close popup button
                button.click()

                # Wait for the popup to close
                time.sleep(1)
                break

    def close(self):
        # Close the browser
        self.driver.quit()
