import pytermgui as ptg 

class TermChat:
    
    def __init__(self):
        self.app = ptg.WindowManager()
        self.app.add(ptg.Window("Hello World!"))
        self.app.run()

