from .component import Component


class LocalBranchHistory(Component):
    WIDTH = 100
    HEIGHT = 20

    def __init__(self, window, x, y, bits):
        super(LocalBranchHistory, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.bits = bits

    def render(self):
        self.draw_text(
            self.x + self.width / 2, self.y + self.height / 4, "PC")
        self.draw_rect(
            self.x, self.y + self.height,
            self.width, self.height,
            fill="white", outline="black")
