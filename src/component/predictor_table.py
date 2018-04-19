from .component import Component


class PredictorTable(Component):
    CELL_WIDTH = 40
    CELL_HEIGHT = 15

    def __init__(self, window, x, y, label, bits):
        super(PredictorTable, self).__init__(window, x, y, self.CELL_WIDTH, self.CELL_HEIGHT * bits)
        self.label = label
        self.bits = bits

    def render(self):
        self.draw_text(
            self.x + self.width / 2, self.y + self.height / 4, self.label)
        for i in range(0, 2 ** self.bits):
            self.draw_rect(
                self.x, self.y + self.CELL_HEIGHT * (i + 1),
                self.CELL_WIDTH, self.CELL_HEIGHT,
                fill="white", outline="black")
