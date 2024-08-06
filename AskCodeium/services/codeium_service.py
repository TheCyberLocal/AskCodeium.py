class CodeiumService:
    @staticmethod
    async def send_request(chat_thread, query):
        context = chat_thread.get_context()
        # Simulate sending a request to Codeium and getting a response
        response = f"Response based on context: {context} and query: {query}"
        return response
