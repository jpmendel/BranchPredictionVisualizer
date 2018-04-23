from .component import Component


class GlobalBranchHistory(Component):
    CELL_WIDTH = 80
    CELL_HEIGHT = 20

    def __init__(self, window, x, y, bits):
        super(GlobalBranchHistory, self).__init__(window, x, y, self.CELL_WIDTH, self.CELL_HEIGHT * 2)
        self.bits = bits

    def render(self):
        self.draw_text(
            self.x + self.CELL_WIDTH * 0.50,
            self.y + self.CELL_HEIGHT * 0.50,
            "Global Branch History")
        self.draw_rect(
            self.x, self.y + self.CELL_HEIGHT,
            self.CELL_WIDTH, self.CELL_HEIGHT,
            fill="white", outline="black")
