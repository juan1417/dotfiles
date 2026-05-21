import pytermgui as ptg 

class TermChat:
    
    def __init__(self):
        self.app = ptg.WindowManager()
        with self.app as manager:
            self.GetInput()
            manager.add(self.chat_window)
            manager.add(self.input_window)

    def GetInput(self):
        
