RULES = "1. Click <PlayNext> to start the game\n2. Enter the word in the input\n3. Click <Check> for " \
            "result\n4. Click <Replay> to reply\n5. Click <meaning> to get the word's definition"


def input_frame(root, tk, cmd):
    frame_top = tk.Frame(root, bg='#22e5d5')
    frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.3)

    input_field = tk.Entry(frame_top, textvariable="Click PlayNext to start", bg='#8cfff1')
    input_field.place(relx=0.1, rely=0.5, relwidth=0.55, relheight=0.3)

    button_check = tk.Button(frame_top, text="Check", command=lambda: cmd.validate_result(input_field.get()))
    button_check.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.3)

    frame_buttum = tk.Frame(root, bg='#22e5d5')
    frame_buttum.place(relx=0, rely=0.3, relwidth=1, relheight=0.3)

    button_replay = tk.Button(frame_buttum, text="Replay", command=cmd.replay)
    button_replay.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.5)

    frame_bottum = tk.Frame(root, bg='#8cfff1')
    frame_bottum.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

    meaning = tk.Label(frame_bottum, text=RULES, bg='#affff4', wraplength=350, justify="left")
    meaning.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.8)

    button_meaning = tk.Button(frame_buttum, text="Meaning", command=lambda: cmd.find_meaning(meaning))
    button_meaning.place(relx=0.7, rely=0, relwidth=0.2, relheight=0.5)

    button_play = tk.Button(frame_buttum, text="PlayNext", command=lambda: cmd.spell_the_word(meaning, input_field))
    button_play.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.5)
