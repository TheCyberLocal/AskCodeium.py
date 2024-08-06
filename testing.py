from AskCodeium.utils.browser_manager import BrowserManager

try:
    bgBrowser = BrowserManager()
    bgBrowser.perform_action("http://example.com")
    bgBrowser.close()
except Exception as e:
    print(e)
