from .component import Component
from .predictor_table import PredictorTable
from .local_branch_history import LocalBranchHistory
from .global_branch_history import GlobalBranchHistory
#from .multiplexer import Multiplexer

class TournamentPredictor(Component):
    WIDTH = 400
    HEIGHT = 300

    def __init__(self, window, x, y):
        super(TournamentPredictor, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.index_table = PredictorTable(
            self.window,
            self.x + self.width,
            self.y,
            "Index", 2)
        self.branch_history_table = PredictorTable(
            self.window,
            self.x + self.width * 0.25,
            self.y,
            "BHT", 2)
        self.pattern_history_table = PredictorTable(
            self.window,
            self.x + self.width * 0.50,
            self.y,
            "PHT", 2)
        self.meta_predictor = PredictorTable(
            self.window,
            self.x + self.width * 0.75,
            self.y,
            "Meta", 2)
        self.local_branch_history = LocalBranchHistory(
            self.window,
            self.x,
            self.y + 50,
            2)
        self.global_branch_history = GlobalBranchHistory(
            self.window,
            self.x + self.width * 0.75,
            self.y,
            2)

    def render(self):
        self.index_table.render()
        self.branch_history_table.render()
        self.pattern_history_table.render()
        self.meta_predictor.render()
        self.local_branch_history.render()
        self.global_branch_history.render()
