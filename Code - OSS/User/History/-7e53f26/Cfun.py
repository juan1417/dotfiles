import pytermgui as ptg 

class TermChat:
    
    def __init__(self):
        self.app = ptg.WindowManager()
        with self.app as manager:
            self.GetInput()
            manager.add(self.chat_window)
            manager.add(self.input_window)

    def GetInput(self):
        self.chat_window = ptg.Window(title="Chat Window")
        self.input_window = ptg.Window(title="Input Window")
        self.input_field = ptg.InputField()
        self.input_window._add_widget(self.input_field)
        self.input_field.handle_key(ptg.keys.ENTER, self.SendMessage)
