from .component import Component
from .instruction_entry import InstructionEntry

class InstructionTable(Component):
    NUM_VISIBLE = 8
    WIDTH = InstructionEntry.WIDTH * 2
    HEIGHT = InstructionEntry.HEIGHT * (NUM_VISIBLE + 1)
    def __init__(self, window, x, y, instructions):
        super(InstructionTable, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.current_instruction = 0
        self.instruction_header = InstructionEntry(
            self.window, self.x, self.y, "PC", "Instruction"
        )
        self.instructions = []
        for i in range(0, len(instructions)):
            instruction = InstructionEntry(
                self.window, self.x, self.y + InstructionEntry.HEIGHT * (i + 1),
                i, instructions[i])
            self.instructions.append(instruction)

    def render(self):
        for i in range(0, self.NUM_VISIBLE + 1):
            color = "yellow" if i == 1 else "white"
            self.window.create_rectangle(
                self.x, self.y + (i * InstructionEntry.HEIGHT),
                self.x + InstructionEntry.WIDTH, self.y + ((i + 1) * InstructionEntry.HEIGHT),
                fill=color, outline="black")
            self.window.create_rectangle(
                self.x + InstructionEntry.WIDTH, self.y + (i * InstructionEntry.HEIGHT),
                self.x + InstructionEntry.WIDTH * 2, self.y + ((i + 1) * InstructionEntry.HEIGHT),
                fill=color, outline="black")
        self.instruction_header.render()
        for i in range(self.current_instruction, self.current_instruction + self.NUM_VISIBLE):
            if i < len(self.instructions):
                if i == self.current_instruction:
                    self.instructions[i].current = True
                else:
                    self.instructions[i].current = False
                self.instructions[i].y = self.y + InstructionEntry.HEIGHT * (i - self.current_instruction + 1)
                self.instructions[i].render()

    def set_instruction(self, instruction):
        self.current_instruction = instruction
