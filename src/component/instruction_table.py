from src.component.component import Component
from src.component.instruction_entry import InstructionEntry

class InstructionTable(Component):
    NUM_VISIBLE = 8
    def __init__(self, window, x, y, instructions):
        super(InstructionTable, self).__init__(window, x, y)
        self.instructions = []
        for i in range(0, len(instructions)):
            instruction = InstructionEntry(
                self.window, self.x,
                self.y + InstructionEntry.HEIGHT * i,
                instructions[i])
            self.instructions.append(instruction)

    def update(self):
        for instruction in self.instructions:
            instruction.update()

    def render(self):
        self.window.create_rectangle(
            self.x, self.y,
            self.x + InstructionEntry.WIDTH,
            self.y + InstructionEntry.HEIGHT * self.NUM_VISIBLE,
            fill="gray", outline="black")
        for i in range(0, self.NUM_VISIBLE if self.NUM_VISIBLE < len(self.instructions) else len(self.instructions)):
            if i == 0:
                self.instructions[i].current = True
            self.instructions[i].render()

    def next_instruction(self):
        if len(self.instructions) > 0:
            self.instructions.pop(0)
            for instruction in self.instructions:
                instruction.y -= instruction.HEIGHT
