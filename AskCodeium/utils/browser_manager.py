from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class BrowserManager:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def perform_action(self, url):
        print(f"Opening {url}")
        self.driver.get(url)
        time.sleep(2)  # Wait for the page to load
        print("Page title:", self.driver.title)
        return self.driver.title

    def close(self):
        self.driver.quit()
        print("Browser closed")

# Example usage:
if __name__ == "__main__":
    browser_manager = BrowserManager()
    browser_manager.perform_action("https://www.example.com")
    browser_manager.close()
