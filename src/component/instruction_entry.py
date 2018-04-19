from .component import Component


class InstructionEntry(Component):
    WIDTH = 160
    HEIGHT = 40

    def __init__(self, window, x, y, pc, instruction):
        super(InstructionEntry, self).__init__(window, x, y, self.WIDTH, self.HEIGHT)
        self.pc = pc
        self.instruction = instruction
        self.focus = False
        self.header = False

    def render(self):
        font_size = "16" if self.focus else "12"
        offset = 15 if self.focus else 0
        style = " bold" if self.header else ""
        self.draw_text(
            self.x + self.width / 2 - offset, self.y + self.height / 2,
            text=self.pc, font="TkDefaultFont " + font_size + style, anchor="center")
        self.draw_text(
            self.x + self.width + self.width / 2 + offset, self.y + self.height / 2,
            text=self.instruction, font="TkDefaultFont " + font_size + style, anchor="center")
