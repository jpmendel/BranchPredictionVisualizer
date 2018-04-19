from .component import Component


class GlobalBranchHistory(Component):
    WIDTH = 80
    HEIGHT = 15

    def __init__(self, window, x, y, bits):
        super(GlobalBranchHistory, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.bits = bits

    def render(self):
        self.draw_text(
            self.x + self.width / 2, self.y + self.height / 4, "Global Branch History")
        self.draw_rect(
            self.x, self.y + self.height,
            self.width, self.height,
            fill="white", outline="black")
