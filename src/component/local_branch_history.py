from .component import Component


class LocalBranchHistory(Component):
    CELL_WIDTH = 100
    CELL_HEIGHT = 20

    def __init__(self, window, x, y, history):
        super(LocalBranchHistory, self).__init__(window, x, y, self.CELL_WIDTH, self.CELL_HEIGHT * 2)
        self.history = history

    def render(self):
        self.draw_text(
            self.x + self.CELL_WIDTH * 0.50,
            self.y + self.CELL_HEIGHT * 0.50,
            "PC")
        self.draw_rect(
            self.x, self.y + self.CELL_HEIGHT,
            self.CELL_WIDTH, self.CELL_HEIGHT,
            fill="white", outline="black")
        self.draw_text(
            self.x + self.CELL_WIDTH * 0.75,
            self.y + self.CELL_HEIGHT * 1.50,
            format(self.history, "02b"))
        self.draw_line(
            self.x + self.CELL_WIDTH * 0.62,
            self.y + self.CELL_HEIGHT,
            self.x + self.CELL_WIDTH * 0.62,
            self.y + self.CELL_HEIGHT * 2)
        self.draw_line(
            self.x + self.CELL_WIDTH * 0.86,
            self.y + self.CELL_HEIGHT,
            self.x + self.CELL_WIDTH * 0.86,
            self.y + self.CELL_HEIGHT * 2)
