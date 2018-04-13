from tkinter import *
from src.component.instruction_table import InstructionTable

class App:
    TITLE = "Branch Prediction Visualizer"
    ICON = None
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    DELAY = 50
    def __init__(self, window):
        self.window = window
        with open("data/instructionTest.txt", "r") as instruction_file:
            instructions = instruction_file.readlines()
        self.instruction_table = InstructionTable(self.window, 100, 100, instructions)

    def update(self):
        self.instruction_table.next_instruction()

    def render(self):
        self.instruction_table.render()

    def clear(self):
        self.window.delete(ALL)

    def l_mouse_pressed(self, mouse_x, mouse_y):
        pass

    def r_mouse_pressed(self, mouse_x, mouse_y):
        pass

    def key_pressed(self, character, symbol):
        pass

    def key_released(self, character, symbol):
        pass

def l_mouse_pressed(event):
    app.l_mouse_pressed(event.x, event.y)

def r_mouse_pressed(event):
    app.r_mouse_pressed(event.x, event.y)

def key_pressed(event):
    app.key_pressed(event.char, event.keysym)

def key_released(event):
    app.key_released(event.char, event.keysym)

def update_gui():
    app.clear()
    app.update()
    app.render()
    app.window.after(App.DELAY, update_gui)

def init():
    global tk
    global app
    tk = Tk()
    canvas = Canvas(tk, width=App.SCREEN_WIDTH, height=App.SCREEN_HEIGHT)
    canvas.pack()
    tk.resizable(width=0, height=0)
    tk.title(App.TITLE)
    if App.ICON:
        tk.iconbitmap(App.ICON)
    tk.bind("<Button-1>", l_mouse_pressed)
    tk.bind("<Button-3>", r_mouse_pressed)
    tk.bind("<KeyPress>", key_pressed)
    tk.bind("<KeyRelease>", key_released)
    app = App(canvas)

def run():
    init()
    update_gui()
    tk.mainloop()

run()
