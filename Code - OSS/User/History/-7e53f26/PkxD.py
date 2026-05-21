import sys, os

class TermChat:

    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    def __init__(self):
        print(f"Terminal size: {self.width}x{self.height}")
        print("Initializing TermChat...")
