from AskCodeium.utils.browser_manager import BrowserManager

class createChat:
    def __init__(self):
        self._browser = BrowserManager()
        self._history = []

    def send_query(self, query):
        self._browser.send_chat(query)
        response = self._browser.get_chat()
        self._history.append((query, response))
        return response

    def get_history(self):
        return self._history

    def clear_history(self):
        self._browser.clear_chat()
        self._history.clear()

    def close(self):
        self._browser.close()

    def __call__(self, query):
        return self.send_query(query)
