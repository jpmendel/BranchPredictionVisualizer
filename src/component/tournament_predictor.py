from .component import Component
from .predictor_table import PredictorTable
from .local_branch_history import LocalBranchHistory
from .global_branch_history import GlobalBranchHistory
from .multiplexer import Multiplexer

class TournamentPredictor(Component):
    WIDTH = 400
    HEIGHT = 300

    def __init__(self, window, x, y):
        super(TournamentPredictor, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.local_branch_history = LocalBranchHistory(
            self.window,
            self.x,
            self.y,
            2)
        self.branch_history_table = PredictorTable(
            self.window,
            self.local_branch_history.x + self.local_branch_history.width + PredictorTable.CELL_WIDTH * 0.50,
            self.local_branch_history.y,
            "BHT", 2)
        self.multiplexer = Multiplexer(
            self.window,
            self.branch_history_table.x + PredictorTable.CELL_WIDTH * 0.75,
            self.branch_history_table.y + self.branch_history_table.height + PredictorTable.CELL_HEIGHT * 4,
            80, 30)
        self.pattern_history_table = PredictorTable(
            self.window,
            self.multiplexer.x + self.multiplexer.width - PredictorTable.CELL_WIDTH * 0.25,
            self.branch_history_table.y,
            "PHT", 2)
        self.global_branch_history = GlobalBranchHistory(
            self.window,
            self.pattern_history_table.x + PredictorTable.CELL_WIDTH * 0.80,
            self.branch_history_table.y - PredictorTable.CELL_HEIGHT * 3 + 10,
            2)
        self.meta_predictor = PredictorTable(
            self.window,
            self.global_branch_history.x + self.global_branch_history.width - PredictorTable.CELL_WIDTH * 0.20,
            self.branch_history_table.y,
            "Meta", 2)
        self.index_table = PredictorTable(
            self.window,
            self.meta_predictor.x + self.meta_predictor.width + PredictorTable.CELL_WIDTH * 0.50,
            self.branch_history_table.y,
            "Index", 2)

    def render(self):
        self.index_table.render()
        self.branch_history_table.render()
        self.pattern_history_table.render()
        self.meta_predictor.render()
        self.local_branch_history.render()
        self.global_branch_history.render()
        self.multiplexer.render()
