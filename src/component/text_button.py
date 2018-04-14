from .component import Component
from src.data.rgb_color import RGBColor

class ClickState:
    NOT_CLICKED = 0
    PRESS = 1
    RELEASE = 2

class TextButton(Component):
    CLICK_ANIM_LENGTH = 4
    def __init__(self, window, x, y, width=60, height=30, text="Button", color=RGBColor(0xFF), on_click=None):
        super(TextButton, self).__init__(window, x, y, width, height)
        self.text = text
        self.color = color
        self.on_click = on_click
        self.is_clicked = ClickState.NOT_CLICKED
        self.click_counter = 0

    def update(self):
        if self.is_clicked != ClickState.NOT_CLICKED:
            self.animate_click()

    def render(self):
        color = self.color - RGBColor(self.click_counter * 8)
        self.window.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            outline="black", fill=color)
        self.window.create_text(
            self.x + self.width / 2, self.y + self.height / 2,
            text=self.text, fill="white", anchor="center")

    def listen(self, event):
        if self.contains_point(event.x, event.y):
            self.is_clicked = ClickState.PRESS
            self.click_counter = 0
            if self.on_click is not None:
                self.on_click()

    def animate_click(self):
        if self.is_clicked == ClickState.PRESS:
            self.click_counter += 1
            if self.click_counter == self.CLICK_ANIM_LENGTH:
                self.is_clicked = ClickState.RELEASE
        elif self.is_clicked == ClickState.RELEASE:
            self.click_counter -= 1
            if self.click_counter == 0:
                self.is_clicked = ClickState.NOT_CLICKED
                self.click_counter = 0
