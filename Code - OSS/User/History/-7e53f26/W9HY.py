import sys, os

class TermChat:

    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    def __init__(self):
        # clean evything in the terminal and render the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        screen = self.render_screen()
        print(screen)

    def render_screen(self):
        # render the screen
        screen = ""
        for i in range(self.height):
            if i == 0:
                screen += "+" + "-" * (self.width - 2) + "+\n"
            elif i == self.height - 1:
                screen += "+" + "-" * (self.width - 2) + "+\n"
            else:
                screen += "|" + " " * (self.width - 2) + "|\n"
        return screen
