from .component import Component


class PredictorTable(Component):
    CELL_WIDTH = 50
    CELL_HEIGHT = 20

    def __init__(self, window, x, y, label, values):
        super(PredictorTable, self).__init__(window, x, y, self.CELL_WIDTH, self.CELL_HEIGHT * (len(values) + 1))
        self.label = label
        self.values = values

    def render(self):
        self.draw_text(
            self.x + self.CELL_WIDTH * 0.50,
            self.y + self.CELL_HEIGHT * 0.50,
            self.label)
        for i in range(0, len(self.values)):
            self.draw_rect(
                self.x, self.y + self.CELL_HEIGHT * (i + 1),
                self.CELL_WIDTH, self.CELL_HEIGHT,
                fill="white", outline="black")
            self.draw_text(
                self.x + self.CELL_WIDTH * 0.50,
                self.y + self.CELL_HEIGHT * (i + 1) + self.CELL_HEIGHT * 0.50,
                format(self.values[i], "02b"))
