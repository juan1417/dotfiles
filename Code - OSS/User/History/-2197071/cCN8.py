

class Widget:

    childers = []

    def __init__(self, parent=None):
        self.parent = parent

    def add_child(self, child):
        self.childers.append(child)

    def render(self):
        if len(self.childers) > 0:
            auxi = ""
            for child in self.childers:
                auxi += 
            return auxi
        else:
            return ""