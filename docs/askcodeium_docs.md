# 📑 AskCodeium Documentation

### [⇦ Back to Project Overview](../README.md)

## 😅 Don't worry if you can't remember it all!

We have well structured and explanatory docustrings for each function
that allow you to understand exactly how it works by just hovering your mouse.

```py
from AskCodeium import createChat

# You can create multiple independent chat sessions.
chat1 = createChat()
chat2 = createChat()

# Invoke chat instance directly with a query or using the ask method.
response = chat1("In short, what is Machine Learning?")
response = chat1.ask("In short, what is Machine Learning?")
print("Chat1 Response1:", response)

# Chat history can be retrieved using the get_history method.
print("Chat1 History:", chat1.get_history())
# Chat history is returned as list of tuples, [(query1, response1), ...].

# Example output:
# Chat1 History: [
#   ("In short, what is Machine Learning?", "Machine learning is a field of study that gives computers the ability to learn without explicit programming.")
# ]

# Note that the second chat still has no history.
print("Chat2 History:", chat2.get_history())
# Example output: []

# You can clear the chat history using the clear_history method.
chat1.clear_history()
print("Chat1 History:", chat1.get_history())
# Example output: []

# You can close the chat session using the close method.
chat1.close()
chat2.close()
```

Integrate artificial intelligence into your applications effortlessly with AskCodeium, the ultimate API for free and easy-to-use chat interactions. Simplify your development process with seamless thread management and maintain conversational context without the need for user accounts. Start using AskCodeium today!
