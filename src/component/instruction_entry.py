from src.component.component import Component

class InstructionEntry(Component):
    WIDTH = 160
    HEIGHT = 40
    def __init__(self, window, x, y, text):
        super(InstructionEntry, self).__init__(window, x, y)
        self.text = text
        self.current = False

    def update(self):
        pass

    def render(self):
        if self.current:
            color = "yellow"
        else:
            color = "gray"
        self.window.create_rectangle(
            self.x, self.y,
            self.x + self.WIDTH, self.y + self.HEIGHT,
            fill=color, outline="black")
        self.window.create_text(
            self.x + self.WIDTH / 2, self.y + self.HEIGHT / 2 + 10,
            text=self.text, anchor="center")
