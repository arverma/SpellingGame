import random
from difflib import get_close_matches

champion_num = 10


def spell_the_word(engine, word):
    print("Playing......")
    engine.say(word)
    engine.runAndWait()


def read_the_word_from_csv(data):
    not_champion = 1
    while not_champion:
        index = generate_random_number()
        if data.iloc[index, 1] < 10:
            return data.iloc[index, 0], index


def generate_random_number():
    rand_num = random.randint(1, 10010)
    return rand_num


def validate_result(user_input, word):
    if user_input.lower() == word.lower():
        return True
    return False


def save_and_exit(word_data, file_name):
    word_data.to_csv(file_name, index=False)


def record_the_correct_response(index, word_data):
    print("Correct Input :) ")
    word_data["count"][index] += 1
    return word_data


def find_meaning(word, dictionary):
    return dictionary.get(word.lower(), dictionary[get_close_matches(word, dictionary.keys())[0]])