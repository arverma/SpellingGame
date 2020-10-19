import tkinter as tk

WIDTH = 500
HEIGHT = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame_top = tk.Frame(root, bg='#22e5d5')
frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.45)

input_field = tk.Entry(frame_top, bg='#8cfff1')
input_field.pack(expand=True)

frame_bottum = tk.Frame(root, bg='#22e5d5')
frame_bottum.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

button_play = tk.Button(frame_bottum, text="Play")
button_play.pack(side="left", expand=True)

button_replay = tk.Button(frame_bottum, text="Replay")
button_replay.pack(side="left", expand=True)

button_check = tk.Button(frame_bottum, text="Check")
button_check.pack(side="left", expand=True)

button_meaning = tk.Button(frame_bottum, text="Meaning")
button_meaning.pack(side="left", expand=True)

button_next = tk.Button(frame_bottum, text="Next")
button_next.pack(side="left", expand=True)

root.mainloop()
