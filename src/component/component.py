from tkinter import *

class Component(object):

    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains_point(self, x, y):
        return (x > self.x and x < self.x + self.width
            and y > self.y and y < self.y + self.height)
