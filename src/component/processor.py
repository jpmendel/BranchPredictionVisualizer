from .component import Component
from .instruction_table import InstructionTable
from .text_button import TextButton

class Processor(Component):
    def __init__(self, window, instruction_file):
        super(Processor, self).__init__(window, 0, 0, 1000, 600)
        self.instructions = []
        with open(instruction_file, "r") as instruction_file_open:
            self.instructions = instruction_file_open.read().splitlines()
        self.current_instruction = 0
        self.play = False
        self.play_counter = 0
        self.instruction_table = InstructionTable(self.window, 100, 100, self.instructions)
        self.back_button = TextButton(
            self.window,
            self.instruction_table.x + 30,
            480, 60, 30, "<")
        self.play_button = TextButton(
            self.window,
            230, 480, 60, 30, "Play")
        self.forward_button = TextButton(
            self.window,
            self.instruction_table.x + self.instruction_table.width - 90,
            480, 60, 30, ">")

    def update(self):
        if self.play:
            self.play_counter += 1
            if self.play_counter == 2:
                self.next_instruction()
                self.play_counter = 0

    def render(self):
        self.instruction_table.render()
        self.play_button.render()
        self.forward_button.render()
        self.back_button.render()

    def next_instruction(self):
        if self.current_instruction < len(self.instructions) - 1:
            self.current_instruction += 1
            self.instruction_table.set_instruction(self.current_instruction)

    def previous_instruction(self):
        if self.current_instruction > 0:
            self.current_instruction -= 1
            self.instruction_table.set_instruction(self.current_instruction)

    def jump_to_instruction(self, target):
        self.current_instruction = target
        self.instruction_table.set_instruction(self.current_instruction)

    def on_play_click(self, mouse_x, mouse_y):
        if self.play_button.contains_point(mouse_x, mouse_y):
            self.play = not self.play
            self.play_button.text = "Pause" if self.play else "Play"
            self.play_counter = 0

    def on_forward_click(self, mouse_x, mouse_y):
        if self.forward_button.contains_point(mouse_x, mouse_y):
            self.next_instruction()

    def on_back_click(self, mouse_x, mouse_y):
        if self.back_button.contains_point(mouse_x, mouse_y):
            self.previous_instruction()
