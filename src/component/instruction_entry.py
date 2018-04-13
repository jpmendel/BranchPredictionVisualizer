from .component import Component

class InstructionEntry(Component):
    WIDTH = 160
    HEIGHT = 40
    def __init__(self, window, x, y, pc, instruction):
        super(InstructionEntry, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.pc = pc
        self.instruction = instruction

    def render(self):
        self.window.create_text(
            self.x + self.width / 2, self.y + self.height / 2,
            text=self.pc, anchor="center")
        self.window.create_text(
            self.x + self.width + self.width / 2, self.y + self.height / 2,
            text=self.instruction, anchor="center")
