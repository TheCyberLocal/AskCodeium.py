from AskCodeium.services.create_chat import createChat

try:
    # Create two chat sessions
    chat1 = createChat()
    chat2 = createChat()

    # Send queries to chat1
    response1_1 = chat1("What makes python a data science language?")
    print('\nChat1 Response1:', response1_1)
    print('\nChat1 History:', chat1.get_history())

    # Send queries to chat2
    response2_1 = chat2("What is the capital of France?")
    print('\nChat2 Response1:', response2_1)
    print('\nChat2 History:', chat2.get_history())

    # Send another query to chat1
    response1_2 = chat1("Explain machine learning in simple terms.")
    print('\nChat1 Response2:', response1_2)
    print('\nChat1 History:', chat1.get_history())

    # Send another query to chat2
    response2_2 = chat2("Describe the Eiffel Tower.")
    print('\nChat2 Response2:', response2_2)
    print('\nChat2 History:', chat2.get_history())

    # Clear chat1 history
    chat1.clear_history()
    print('\nChat1 History after clearing:', chat1.get_history())

    # Close chat sessions
    chat1.close()
    chat2.close()
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
