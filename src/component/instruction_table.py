from .component import Component
from .instruction_entry import InstructionEntry

class InstructionTable(Component):
    NUM_VISIBLE = 7
    WIDTH = InstructionEntry.WIDTH * 2
    HEIGHT = InstructionEntry.HEIGHT * (NUM_VISIBLE + 1)
    def __init__(self, window, x, y, instructions):
        super(InstructionTable, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.current_instruction = 0
        self.instruction_header = InstructionEntry(
            self.window, self.x, self.y, "PC", "Instruction")
        self.instruction_header.header = True
        self.instructions = []
        for i in range(0, len(instructions)):
            instruction = InstructionEntry(
                self.window, self.x, self.y + InstructionEntry.HEIGHT * (i + 1),
                i, instructions[i])
            self.instructions.append(instruction)

    def render(self):
        i = 0
        for j in range(0, 2):
            self.window.create_rectangle(
                self.x + (j * InstructionEntry.WIDTH),
                self.y,
                self.x + ((j + 1) * InstructionEntry.WIDTH),
                self.y + InstructionEntry.HEIGHT,
                fill="gray", outline="black")
            self.instruction_header.render()
        i += 1
        while i < self.NUM_VISIBLE // 2 + 1:
            for j in range(0, 2):
                self.window.create_rectangle(
                    self.x + (j * InstructionEntry.WIDTH),
                    self.y + (i * InstructionEntry.HEIGHT),
                    self.x + ((j + 1) * InstructionEntry.WIDTH),
                    self.y + ((i + 1) * InstructionEntry.HEIGHT),
                    fill="white", outline="black")
                index = self.current_instruction - self.NUM_VISIBLE // 2 + i - 1
                if index >= 0 and index < len(self.instructions):
                    self.instructions[index].y = (
                        self.y + (i * InstructionEntry.HEIGHT))
                    self.instructions[index].focus = False
                    self.instructions[index].render()
            i += 1
        for j in range(0, 2):
            offset_start = 30 if j == 0 else 0
            offset_end = 30 if j == 1 else 0
            self.window.create_rectangle(
                self.x + (j * InstructionEntry.WIDTH) - offset_start,
                self.y + ((self.NUM_VISIBLE // 2 + 1) * InstructionEntry.HEIGHT),
                self.x + ((j + 1) * InstructionEntry.WIDTH) + offset_end,
                self.y + ((self.NUM_VISIBLE // 2 + 2) * InstructionEntry.HEIGHT) + 15,
                fill="#FFFFDD", outline="black")
            index = self.current_instruction
            if index >= 0 and index < len(self.instructions):
                self.instructions[index].y = (
                    self.y + ((self.NUM_VISIBLE // 2 + 1) * InstructionEntry.HEIGHT) + 7.5)
                self.instructions[index].focus = True
                self.instructions[index].render()
        i += 1
        while i < self.NUM_VISIBLE + 1:
            for j in range(0, 2):
                self.window.create_rectangle(
                    self.x + (j * InstructionEntry.WIDTH),
                    self.y + (i * InstructionEntry.HEIGHT) + 15,
                    self.x + ((j + 1) * InstructionEntry.WIDTH),
                    self.y + ((i + 1) * InstructionEntry.HEIGHT) + 15,
                    fill="white", outline="black")
                index = self.current_instruction + i - self.NUM_VISIBLE // 2 - 1
                if index >= 0 and index < len(self.instructions):
                    self.instructions[index].y = (
                        self.y + (i * InstructionEntry.HEIGHT) + 15)
                    self.instructions[index].focus = False
                    self.instructions[index].render()
            i += 1
