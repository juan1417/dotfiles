from textual.app import App
from textual.color import Color
from textual.widgets import Header, Footer, Input

class TermChat(App):

    def __init__(self):
        super().__init__()
     
    def on_mount(self):
        self.screen.styles.background_tint = "black 20%"