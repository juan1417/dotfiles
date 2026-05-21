

class Widget:

    childers = []

    def __init__(self, parent=None):
        self.parent = parent

    def add_child(self, child):
        self.childers.append(child)

    def render(self):
        if len(self.childers) > 0:
            for child in self.childers:
                child.render()
