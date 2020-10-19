from gtts import gTTS
import json
import pandas as pd
import random
from pygame import mixer
from difflib import get_close_matches
from tkinter import messagebox
import playsound

pd.options.mode.chained_assignment = None
champion_num = 10

words_file_name = "../Data/words.csv"
dict_file_name = "../Data/dictionary.json"


def generate_random_number():
    rand_num = random.randint(1, 10010)
    return rand_num


class Game:
    def __init__(self, root):
        self.root = root
        self.data = pd.read_csv(words_file_name)
        self.dict_data = json.load(open(dict_file_name))
        self.word = "Start"

    def spell_the_word(self, meaning, input_field):
        meaning.config(text="")
        input_field.config(text="")
        self.word, index = self.read_the_word_from_csv()
        print("Playing......")
        try:
            speech = gTTS(text=self.word, lang='en', slow=False)
            speech.save("voice.mp3")
        except:
            raise Exception("Error: Text to Speech")
        try:
            playsound.playsound("voice.mp3")
        except:
            raise Exception("Error: Playing")

    def replay(self):
        mixer.init()
        mixer.music.load('voice.mp3')
        mixer.music.play()

    def read_the_word_from_csv(self):
        not_champion = 1
        while not_champion:
            index = generate_random_number()
            if self.data.iloc[index, 1] < 10:
                return self.data.iloc[index, 0], index

    def validate_result(self, user_input):
        if user_input.lower() == self.word.lower():
            messagebox.showinfo("Result", "Correct")
        else:
            messagebox.showinfo("Result", "Incorrect")

    def save_and_exit(self):
        self.data.to_csv(words_file_name, index=False)

    def record_the_correct_response(self, index):
        print("Correct Input :) ")
        self.data["count"][index] += 1
        return self.data

    def find_meaning(self, meaning):
        meaning.config(
            text={self.word: self.dict_data.get(
                self.word.lower(), self.dict_data[get_close_matches(
                    self.word, self.dict_data.keys())[0]]
            )
            }
        )
