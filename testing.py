from AskCodeium.utils.browser_manager import BrowserManager

try:
    bgBrowser = BrowserManager()
    bgBrowser.send_text("What makes python a data science language?")
    response = bgBrowser.get_chat()
    print('\nrep1', response)
    bgBrowser.send_text("What did I last ask about?")
    response = bgBrowser.get_chat()
    print('\nrep2', response)
    bgBrowser.send_clear()
    bgBrowser.send_text("What did I last ask about?")
    response = bgBrowser.get_chat()
    print('\nrep3', response)
    bgBrowser.send_text("That's fine. Thanks for your help!")
    response = bgBrowser.get_chat()
    print('\nrep4', response)
    bgBrowser.close()
except Exception as e:
    print(e)
