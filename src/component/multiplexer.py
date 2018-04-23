from .component import Component


class Multiplexer(Component):
    def __init__(self, window, x, y, width, height):
        super(Multiplexer, self).__init__(window, x, y, width, height)

    def render(self):
        self.draw_line(self.x, self.y, self.x + 10, self.y + self.height)
        self.draw_line(self.x, self.y, self.x + self.width, self.y)
        self.draw_line(self.x + self.width, self.y, self.x + self.width - 10, self.y + self.height)
        self.draw_line(self.x + 10, self.y + self.height, self.x + self.width - 10, self.y + self.height)
        self.draw_text(self.x + self.width * 0.25, self.y + self.height * 0.50, "0")
        self.draw_text(self.x + self.width * 0.75, self.y + self.height * 0.50, "1")
