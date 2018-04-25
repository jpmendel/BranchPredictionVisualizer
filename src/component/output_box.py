from .component import Component


class OutputBox(Component):

    def __init__(self, window, x, y, width=100, height=50, text="No Output"):
        super(OutputBox, self).__init__(window, x, y, width, height)
        self.text = text

    def update(self):
        pass

    def render(self):
        self.draw_rect(
            self.x, self.y, self.width, self.height,
            fill="white", outline="black")
        self.draw_text(
            self.x + self.width / 2, self.y + self.height / 2,
            text=self.text, fill="black", anchor="center")
