word_list = ["Stellenberg","Joburg","Pietermaritzburg"]
import random

chosen_word = random.choice(word_list)

user_word = input("guess a letter and assign an answer: ")

for word in chosen_word:
    if user_word == chosen_word:
        print("Right")
    else:
        print("false")