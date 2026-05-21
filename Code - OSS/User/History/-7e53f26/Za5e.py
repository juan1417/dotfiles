import pytermgui as ptg 

class TermChat:
    
    def __init__(self):
        self.app = ptg.WindowManager()
        with self.app as manager:
            self.chat_window = ptg.Window(title="Chat")
            self.input_window = ptg.Window(title="Input")
            manager.add(self.chat_window)
            manager.add(self.input_window)


    def GetInput(self):
        return self.input_window.get_input()

    def send_message(self, message):
        self.chat_window.add(ptg.Label(message))
