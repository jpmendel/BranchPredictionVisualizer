from .component import Component

class TextButton(Component):
    def __init__(self, window, x, y, width, height, text):
        super(TextButton, self).__init__(window, x, y, width, height)
        self.text = text

    def render(self):
        self.window.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            outline="black", fill="gray")
        self.window.create_text(
            self.x + self.width / 2, self.y + self.height / 2,
            text=self.text, anchor="center")
