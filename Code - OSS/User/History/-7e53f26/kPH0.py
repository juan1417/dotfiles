import pytermgui as ptg 

class TermChat:
    """
    A chat bot connected to a terminal interface using ollamana like assistent. 
    It allows users to interact with the bot through a command-line interface, providing a seamless and 
    efficient way to communicate and receive responses.
    """
    _window: ptg.Window 
    def __init__(self):
        self._window = ptg.Window()
        self._window.set_title("TermChat - Your Terminal Chat Bot")
        self._window.ad(ptg.Label("Welcome to TermChat! Type your message below:"))
        self._window.add(ptg.InputField())
        self._window.show()

    def get_user_input(self):
        """
        Retrieves user input from the terminal interface.
        """
        return self._window.get_input()

