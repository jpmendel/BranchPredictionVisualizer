from .component import Component
from .predictor_table import PredictorTable
from .local_branch_history import LocalBranchHistory
from .global_branch_history import GlobalBranchHistory
from .multiplexer import Multiplexer
import random

class TournamentPredictor(Component):
    WIDTH = 400
    HEIGHT = 300

    def __init__(self, window, x, y):
        super(TournamentPredictor, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.local_branch_history = 0
        self.global_branch_history = ["0", "0"]
        self.branch_history_table = [2, 2, 2, 2]
        self.pattern_history_table = [2, 2, 2, 2]
        self.meta_predictor = [random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)]
        self.result = "Not Taken"
        self.local_history_component = LocalBranchHistory(
            self.window,
            self.x,
            self.y,
            self.local_branch_history)
        self.bht_component = PredictorTable(
            self.window,
            self.local_history_component.x + self.local_history_component.width + PredictorTable.CELL_WIDTH * 0.50,
            self.local_history_component.y,
            "BHT", self.branch_history_table)
        self.multiplexer = Multiplexer(
            self.window,
            self.bht_component.x + PredictorTable.CELL_WIDTH * 0.25,
            self.bht_component.y + self.bht_component.height + PredictorTable.CELL_HEIGHT * 2,
            100, 30)
        self.pht_component = PredictorTable(
            self.window,
            self.multiplexer.x + self.multiplexer.width - PredictorTable.CELL_WIDTH * 0.75,
            self.bht_component.y,
            "PHT", self.pattern_history_table)
        self.global_history_component = GlobalBranchHistory(
            self.window,
            self.pht_component.x + PredictorTable.CELL_WIDTH * 0.80,
            self.bht_component.y - PredictorTable.CELL_HEIGHT * 3 + 10,
            self.global_branch_history)
        self.meta_component = PredictorTable(
            self.window,
            self.global_history_component.x + self.global_history_component.width - PredictorTable.CELL_WIDTH * 0.20,
            self.bht_component.y,
            "Meta", self.meta_predictor)
        self.index_table = PredictorTable(
            self.window,
            self.meta_component.x + self.meta_component.width + PredictorTable.CELL_WIDTH * 0.50,
            self.bht_component.y,
            "Index", [0, 1, 2, 3])

    def render(self):
        self.local_history_component.render()
        self.bht_component.render()
        self.multiplexer.render()
        self.pht_component.render()
        self.global_history_component.render()
        self.meta_component.render()
        self.index_table.render()
        self.draw_line(
            self.local_history_component.x + self.local_history_component.width * 0.50,
            self.local_history_component.y + self.local_history_component.height,
            self.local_history_component.x + self.local_history_component.width * 0.50,
            self.local_history_component.y + self.local_history_component.height + PredictorTable.CELL_HEIGHT * 1.5)
        self.draw_line(
            self.local_history_component.x + self.local_history_component.width * 0.50,
            self.local_history_component.y + self.local_history_component.height + PredictorTable.CELL_HEIGHT * 1.5,
            self.local_history_component.x + self.local_history_component.width + PredictorTable.CELL_WIDTH * 0.50,
            self.local_history_component.y + self.local_history_component.height + PredictorTable.CELL_HEIGHT * 1.5)
        self.draw_line(
            self.bht_component.x + self.bht_component.width * 0.50,
            self.bht_component.y + self.bht_component.height,
            self.bht_component.x + self.bht_component.width * 0.50,
            self.bht_component.y + self.bht_component.height + PredictorTable.CELL_HEIGHT * 2)
        self.draw_line(
            self.pht_component.x + self.pht_component.width * 0.50,
            self.pht_component.y + self.pht_component.height,
            self.pht_component.x + self.pht_component.width * 0.50,
            self.pht_component.y + self.pht_component.height + PredictorTable.CELL_HEIGHT * 2)
        self.draw_line(
            self.multiplexer.x + self.multiplexer.width * 0.50,
            self.multiplexer.y + self.multiplexer.height,
            self.multiplexer.x + self.multiplexer.width * 0.50,
            self.multiplexer.y + self.multiplexer.height + PredictorTable.CELL_HEIGHT)
        self.draw_line(
            self.global_history_component.x + self.global_history_component.width * 0.5,
            self.global_history_component.y + self.global_history_component.height,
            self.global_history_component.x + self.global_history_component.width * 0.5,
            self.global_history_component.y + self.global_history_component.height + PredictorTable.CELL_HEIGHT * 3)
        self.draw_line(
            self.pht_component.x + self.pht_component.width,
            self.pht_component.y + PredictorTable.CELL_HEIGHT * 2.5,
            self.meta_component.x,
            self.meta_component.y + PredictorTable.CELL_HEIGHT * 2.5)
        self.draw_line(
            self.meta_component.x + self.meta_component.width * 0.50,
            self.meta_component.y + self.meta_component.height,
            self.meta_component.x + self.meta_component.width * 0.50,
            self.multiplexer.y + self.multiplexer.height * 0.50)
        self.draw_line(
            self.meta_component.x + self.meta_component.width * 0.50,
            self.multiplexer.y + self.multiplexer.height * 0.50,
            self.multiplexer.x + self.multiplexer.width - 5,
            self.multiplexer.y + self.multiplexer.height * 0.50)
        self.draw_text(
            self.multiplexer.x + self.multiplexer.width * 0.50,
            self.multiplexer.y + self.multiplexer.height + PredictorTable.CELL_HEIGHT * 2,
            self.result, font="TKDefaultFont 16")

    def update_global_history(self, branch):
        self.global_branch_history.insert(0, str(branch))
        self.global_branch_history.pop()

    def update_local_history(self, pc_index):
        self.local_branch_history = pc_index

    def take_branch(self, actual):
        bht_result = self.get_branch_prediction(self.branch_history_table, self.local_branch_history)
        pht_result = self.get_branch_prediction(self.pattern_history_table, self.get_global_branch_history())
        meta = self.meta_predictor[self.get_global_branch_history()]
        prediction = pht_result if meta > 1 else bht_result
        self.result = "Taken" if prediction == 1 else "Not Taken"
        if actual == 1:
            self.increment_history(self.branch_history_table, self.local_branch_history)
            self.increment_history(self.pattern_history_table, self.get_global_branch_history())
        else:
            self.decrement_history(self.branch_history_table, self.local_branch_history)
            self.decrement_history(self.pattern_history_table, self.get_global_branch_history())
        if actual == prediction:
            self.increment_history(self.meta_predictor, self.get_global_branch_history())
        else:
            self.decrement_history(self.meta_predictor, self.get_global_branch_history())
        self.update_global_history(actual)
        return prediction

    def get_branch_prediction(self, history, index):
        if history[index] > 1:
            return 1
        else:
            return 0

    def increment_history(self, history, index):
        if history[index] < 3:
            history[index] += 1

    def decrement_history(self, history, index):
        if history[index] > 0:
            history[index] -= 1

    def get_global_branch_history(self):
        return int("".join(self.global_branch_history), 2)

    def set_local_branch_history(self, history):
        self.local_branch_history = history
        self.local_history_component.history = history
