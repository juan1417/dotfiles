import sys, os



class TermChat:

    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    widgets = []

    def __init__(self):
        # clean evything in the terminal and render the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        screen = self.render_screen()
        print(screen)

    def render_screen(self):
        # render the screen
        screen = ""
        if len(self.widgets) > 0:
            for widget in self.widgets:
                screen += widget
        else:
            screen += ""
        return screen

    async def on_key_press(self):
        # get the key pressed by the user and handle it
        key = sys.stdin.read(1)
        return key.__str__()

    def run(self):
        # run the app
        while self.on_key_press() != 'q':
            print(self.render_screen())