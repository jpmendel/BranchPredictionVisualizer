from .component import Component
from .instruction_entry import InstructionEntry


class InstructionTable(Component):
    NUM_VISIBLE = 7
    WIDTH = InstructionEntry.WIDTH * 2
    HEIGHT = InstructionEntry.HEIGHT * (NUM_VISIBLE + 1)

    def __init__(self, window, x, y, start_pc, instructions):
        super(InstructionTable, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.current_pc = 0
        self.instruction_header = InstructionEntry(
            self.window, self.x, self.y, "PC", "Instruction")
        self.instruction_header.header = True
        self.instructions = []
        for i in range(0, len(instructions)):
            instruction = InstructionEntry(
                self.window, self.x, self.y + InstructionEntry.HEIGHT * (i + 1),
                str(i) + " : " + hex((i + start_pc) * 4), instructions[i])
            self.instructions.append(instruction)

    def render(self):
        i = 0
        for j in range(0, 2):
            self.draw_rect(
                self.x + (j * InstructionEntry.WIDTH),
                self.y,
                InstructionEntry.WIDTH,
                InstructionEntry.HEIGHT,
                fill="gray", outline="black")
            self.instruction_header.render()
        i += 1
        while i < self.NUM_VISIBLE // 2 + 1:
            for j in range(0, 2):
                self.draw_rect(
                    self.x + (j * InstructionEntry.WIDTH),
                    self.y + (i * InstructionEntry.HEIGHT),
                    InstructionEntry.WIDTH,
                    InstructionEntry.HEIGHT,
                    fill="white", outline="black")
                index = self.current_pc - self.NUM_VISIBLE // 2 + i - 1
                if index >= 0 and index < len(self.instructions):
                    self.instructions[index].y = (
                        self.y + (i * InstructionEntry.HEIGHT))
                    self.instructions[index].focus = False
                    self.instructions[index].render()
            i += 1
        for j in range(0, 2):
            offset_start = 30 if j == 0 else 0
            self.draw_rect(
                self.x + (j * InstructionEntry.WIDTH) - offset_start,
                self.y + ((self.NUM_VISIBLE // 2 + 1) * InstructionEntry.HEIGHT),
                InstructionEntry.WIDTH + 30,
                InstructionEntry.HEIGHT + 15,
                fill="#FFFFDD", outline="black")
            index = self.current_pc
            if index >= 0 and index < len(self.instructions):
                self.instructions[index].y = (
                    self.y + ((self.NUM_VISIBLE // 2 + 1) * InstructionEntry.HEIGHT) + 7.5)
                self.instructions[index].focus = True
                self.instructions[index].render()
        i += 1
        while i < self.NUM_VISIBLE + 1:
            for j in range(0, 2):
                self.draw_rect(
                    self.x + (j * InstructionEntry.WIDTH),
                    self.y + (i * InstructionEntry.HEIGHT) + 15,
                    InstructionEntry.WIDTH,
                    InstructionEntry.HEIGHT,
                    fill="white", outline="black")
                index = self.current_pc + i - self.NUM_VISIBLE // 2 - 1
                if index >= 0 and index < len(self.instructions):
                    self.instructions[index].y = (
                        self.y + (i * InstructionEntry.HEIGHT) + 15)
                    self.instructions[index].focus = False
                    self.instructions[index].render()
            i += 1
