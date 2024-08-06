import uuid

class ChatThread:
    def __init__(self):
        self.thread_id = str(uuid.uuid4())
        self.history = []

    def add_message(self, message):
        self.history.append(message)

    def clear_history(self):
        self.history = []

    def get_context(self):
        return " ".join(self.history)
