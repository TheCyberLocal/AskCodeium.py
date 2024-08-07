from AskCodeium import createChat

chat1 = createChat()

print(chat1("What is Python?"))
print(chat1("What is JavaScript?"))
print("Chat1 History:", chat1.get_history())
chat1.clear_history()
print("Chat1 History:", chat1.get_history())
chat1.close()
