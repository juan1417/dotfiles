"""Legacy placeholder for the first widget experiments.

The actual Textual widgets now live in `UI/widgets.py`.
"""


class Widget:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        return "".join(child.render() if hasattr(child, "render") else str(child) for child in self.children)