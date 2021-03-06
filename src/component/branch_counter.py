from .component import Component


class BranchCounter(Component):
    def __init__(self, window, x, y, width, height):
        super(BranchCounter, self).__init__(window, x, y, width, height)
        self.taken_taken = 0
        self.not_taken_taken = 0
        self.taken_not_taken = 0
        self.not_taken_not_taken = 0

    def render(self):
        self.draw_rect(
            self.x, self.y,
            self.width * 0.50, self.height * 0.50,
            fill="white", outline="black")
        self.draw_rect(
            self.x + self.width * 0.50, self.y,
            self.width * 0.50, self.height * 0.50,
            fill="white", outline="black")
        self.draw_rect(
            self.x, self.y + self.height * 0.50,
            self.width * 0.50, self.height * 0.50,
            fill="white", outline="black")
        self.draw_rect(
            self.x + self.width * 0.50, self.y + self.height * 0.50,
            self.width * 0.50, self.height * 0.50,
            fill="white", outline="black")
        self.draw_text(
            self.x + self.width * 0.50,
            self.y - 40,
            "Predicted", font="TKDefaultFont 14 bold")
        self.draw_text(
            self.x - 60,
            self.y + self.height * 0.50,
            "Actual", font="TKDefaultFont 14 bold")
        self.draw_text(
            self.x + self.width * 0.25,
            self.y - 15,
            "T")
        self.draw_text(
            self.x + self.width * 0.25,
            self.y + self.height * 0.25,
            str(self.taken_taken))
        self.draw_text(
            self.x + self.width * 0.75,
            self.y - 15,
            "N")
        self.draw_text(
            self.x + self.width * 0.75,
            self.y + self.height * 0.25,
            str(self.not_taken_taken))
        self.draw_text(
            self.x - 15,
            self.y + self.height * 0.25,
            "T")
        self.draw_text(
            self.x + self.width * 0.25,
            self.y + self.height * 0.75,
            str(self.taken_not_taken))
        self.draw_text(
            self.x - 15,
            self.y + self.height * 0.75,
            "N")
        self.draw_text(
            self.x + self.width * 0.75,
            self.y + self.height * 0.75,
            str(self.not_taken_not_taken))
