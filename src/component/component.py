from tkinter import *


class Component(object):
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains_point(self, x, y):
        return (self.x < x < self.x + self.width
                and self.y < y < self.y + self.height)

    def draw_rect(self, x, y, width, height, fill="black", outline="black"):
        self.window.create_rectangle(
            x, y, x + width, y + height, fill=fill, outline=outline)

    def draw_oval(self, x, y, width, height, fill="black", outline="black"):
        self.window.create_oval(
            x, y, x + width, y + height, fill=fill, outline=outline)

    def draw_line(self, x1, y1, x2, y2, width=1, fill="black"):
        self.window.create_line(
            x1, y1, x2, y2, width=width, fill=fill)

    def draw_text(self, x, y, text, fill="black", font="TKDefaultFont 12", anchor=CENTER):
        self.window.create_text(
            x, y, text=text, fill=fill, font=font, anchor=anchor)

    def draw_image(self, x, y, image, anchor=CENTER):
        self.window.create_image(
            x, y, image, anchor=anchor)
