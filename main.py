from utils import *
import pyttsx3
import json
import pandas as pd
pd.options.mode.chained_assignment = None

words_file_name = "words.csv"
dict_file_name = "dictionary.json"


def main(word_data, dictionary_data, speech_engine):
    user_input = input("Play: <1/0>: ")
    print(user_input, type(user_input))
    exit_game = 1
    if user_input == "1":
        while exit_game:
            word, index = read_the_word_from_csv(word_data)
            listen = 1
            while listen:
                spell_the_word(speech_engine, word)
                try:
                    listen = int(input("Listen again: <1/0>: "))
                except ValueError:
                    listen = 0
            user_input = input("Enter the word: ")
            flag = validate_result(user_input, word)
            if flag:
                word_data = record_the_correct_response(index, word_data)
            else:
                print("Incorrect Input :( ", word)
                user_input = input("Get Meaning: <1/0>: ")
                if user_input == "1":
                    print(word, ": ", find_meaning(word, dictionary_data))
            exit_game = int(input("Exit: <1/0>: "))
        save_and_exit(word_data, words_file_name)
    else:
        print("Wrong input :( Restart!")


if __name__ == "__main__":
    engine = pyttsx3.init()
    data = pd.read_csv(words_file_name)
    dict_data = json.load(open(dict_file_name))

    main(data, dict_data, engine)
