from AskCodeium.utils.browser_manager import BrowserManager

class createChat:
    def __init__(self):
        self._browser = BrowserManager()

    def close(self):
        self._browser.close()

    def get_history(self):
        return self._browser.get_history()

    def clear_history(self):
        self._browser.clear_chat()

    def ask(self, query):
        return self._browser.send_chat(query)

    def __call__(self, query):
        return self.ask(query)
