from AskCodeium.services.create_chat import createChat

try:
    chat = createChat()
    response = chat("What makes python a data science language?")
    print('\nrep1', response)
    print('\nrep2', chat.get_history())
    chat.clear_history()
    print('\nrep3', chat.get_history())
    response = chat("What did I last ask about?")
    print('\nrep4', response)
    print('\nrep5', chat.get_history())
    response = chat("That's fine. Thanks for your help!")
    print('\nrep6', response)
    print('\nrep7', chat.get_history())
    chat.close()
except Exception as e:
    print(e)


# try:
#     bgBrowser = BrowserManager()
#     bgBrowser.send_chat("What makes python a data science language?")
#     response = bgBrowser.get_chat()
#     print('\nrep1', response)
#     bgBrowser.send_chat("What did I last ask about?")
#     response = bgBrowser.get_chat()
#     print('\nrep2', response)
#     bgBrowser.clear_chat()
#     bgBrowser.send_chat("What did I last ask about?")
#     response = bgBrowser.get_chat()
#     print('\nrep3', response)
#     bgBrowser.send_chat("That's fine. Thanks for your help!")
#     response = bgBrowser.get_chat()
#     print('\nrep4', response)
#     bgBrowser.close()
# except Exception as e:
#     print(e)
