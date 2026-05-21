import pytermgui as ptg 

class TermChat:
    
    def __init__(self):
        self.app = ptg.WindowManager()
        with self.app as manager:
            self.chat_window = ptg.Window(title="Chat")
            self.input_window = ptg.Window(title="Input")
            manager.add(self.chat_window)
            manager.add(self.input_window)
