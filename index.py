from tkinter import *
#from src.main import *

class App:
    TITLE = "Branch Prediction Visualizer"
    ICON = None
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    DELAY = 50
    def __init__(self, window):
        self.window = window

    def render(self):
        pass

    def update(self):
        pass

    def mouse_motion(self, mouse_x, mouse_y):
        pass

    def l_mouse_pressed(self, mouse_x, mouse_y):
        pass

    def r_mouse_pressed(self, mouse_x, mouse_y):
        pass

    def key_pressed(self, character, symbol):
        pass

    def key_released(self, character, symbol):
        pass

def mouse_motion(event):
    app.mouse_motion(event.x, event.y)

def l_mouse_pressed(event):
    app.l_mouse_pressed(event.x, event.y)

def r_mouse_pressed(event):
    app.r_mouse_pressed(event.x, event.y)

def key_pressed(event):
    app.key_pressed(event.char, event.keysym)

def key_released(event):
    app.key_released(event.char, event.keysym)

def main_function():
    refresh_gui()
    app.window.after(App.DELAY, main_function)

def refresh_gui():
    app.window.delete(ALL)
    app.update()
    app.render()

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
    tk.bind("<Motion>", mouse_motion)
    tk.bind("<Button-1>", l_mouse_pressed)
    tk.bind("<Button-3>", r_mouse_pressed)
    tk.bind("<KeyPress>", key_pressed)
    tk.bind("<KeyRelease>", key_released)
    app = App(canvas)

def run():
    init()
    main_function()
    tk.mainloop()

run()
