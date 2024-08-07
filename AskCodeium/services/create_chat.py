from AskCodeium.utils.browser_manager import BrowserManager

class createChat:
    def __init__(self, save_history=True):
        self._browser = BrowserManager()
        self._history = []
        self._save_history = save_history

    def close(self):
        self._browser.close()

    def save_history(self, save_history=True):
        self._save_history = save_history == True

    def get_history(self):
        return self._history

    def clear_history(self):
        self._browser.clear_chat()
        self._history.clear()

    def ask(self, query):
        self._browser.send_chat(query)
        response = self._browser.get_chat()
        if (self._save_history):
            self._history.append((query, response))
        return response

    def __call__(self, query):
        return self.ask(query)
