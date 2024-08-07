from AskCodeium.utils.browser_manager import BrowserManager

class createChat:
    """
    A class to create interactive chats with the Codeium.

    Methods:
        - close(): Closes the browser instance.
        - get_history(): Returns the history of queries and responses.
        - clear_history(): Clears the chat history and the browser chat.
        - ask(query): Sends a query and returns the response.
        - __call__(query): Calls the ask method.
    """

    def __init__(self):
        """
        Initializes the createChat instance.

        Example:
            chat = createChat()
        """
        self._browser = BrowserManager()

    def close(self):
        """
        Closes the browser instance.

        Example:
            chat.close()
        """
        self._browser.close()

    def get_history(self):
        """
        Returns the history of queries and their responses.

        Returns:
            list: A list of tuples, [(query1, response1), ...].

        Example:
            history = chat.get_history()
        """
        return self._browser.get_history()

    def clear_history(self):
        """
        Clears the chat history and the browser chat.

        Example:
            chat.clear_history()
        """
        self._browser.clear_chat()

    def ask(self, query):
        """
        Sends a query and returns the response.

        Args:
            query (str): The query to be sent.

        Returns:
            str: The response from the chat.

        Example:
            response = chat.ask("What is Machine Learning?")
        """
        self._browser.send_chat(query)
        return self._browser.get_chat()

    def __call__(self, query):
        """
        Sends a query and returns the response.

        Args:
            query (str): The query to be sent.

        Returns:
            str: The response from the chat.

        Example:
            response = chat("What is Machine Learning?")
        """
        return self.ask(query)
