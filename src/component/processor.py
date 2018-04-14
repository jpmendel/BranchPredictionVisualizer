from .component import Component
from .instruction_table import InstructionTable
from .text_button import TextButton
from src.data.rgb_color import RGBColor

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
            self.instruction_table.x + 30, 450,
            60, 30,
            text="<",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_back_button_click)
        self.play_button = TextButton(
            self.window,
            self.instruction_table.x + self.instruction_table.width / 2 - 30, 450,
            60, 30,
            text="Play",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_play_button_click)
        self.forward_button = TextButton(
            self.window,
            self.instruction_table.x + self.instruction_table.width - 90, 450,
            60, 30,
            text=">",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_forward_button_click)

    def update(self):
        if self.play:
            self.animate_play()
        self.play_button.update()
        self.forward_button.update()
        self.back_button.update()

    def render(self):
        self.instruction_table.render()
        self.play_button.render()
        self.forward_button.render()
        self.back_button.render()

    def play_pause_processor(self):
        self.play = not self.play
        self.play_button.text = "Pause" if self.play else "Play"
        self.play_counter = 0

    def play_processor(self):
        self.play = True
        self.play_button.text = "Pause"
        self.play_counter = 0

    def pause_processor(self):
        self.play = False
        self.play_button.text = "Play"
        self.play_counter = 0

    def next_instruction(self):
        if self.current_instruction < len(self.instructions) - 1:
            self.current_instruction += 1
            self.instruction_table.current_instruction = self.current_instruction

    def previous_instruction(self):
        if self.current_instruction > 0:
            self.current_instruction -= 1
            self.instruction_table.current_instruction = self.current_instruction

    def jump_to_instruction(self, target):
        self.current_instruction = target
        self.instruction_table.current_instruction = self.current_instruction

    def click_events(self, event):
        self.play_button.listen(event)
        self.forward_button.listen(event)
        self.back_button.listen(event)

    def on_play_button_click(self):
        self.play_pause_processor()

    def on_forward_button_click(self):
        self.pause_processor()
        self.next_instruction()

    def on_back_button_click(self):
        self.pause_processor()
        self.previous_instruction()

    def animate_play(self):
        self.play_counter += 1
        if self.play_counter == 2:
            self.next_instruction()
            self.play_counter = 0
            if self.current_instruction == len(self.instructions) - 1:
                self.pause_processor()
