import tkinter as tk
from GUI.frames import *
from GUI.main import Game

WIDTH = 500
HEIGHT = 300

root = tk.Tk(className="SpellingGame")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

game_obj = Game(root)

input_frame(root, tk, game_obj)

root.resizable(False, False)


def on_closing():
    game_obj.save_and_exit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
