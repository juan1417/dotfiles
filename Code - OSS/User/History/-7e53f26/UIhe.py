import sys, os

class TermChat:

    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    def __init__(self):
        pass

    def run(self):
        print("Running TermChat...")