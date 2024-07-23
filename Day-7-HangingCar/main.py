import hanging_words
import random

chosen_word = random.choice(hanging_words.word_list)
word_length = len(chosen_word)

output = []

for list in chosen_word:
    output += '_'

end_game = False
car_parts = 6 

while not end_game:

    guess_the_letter = input('Guess a letter: ').lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if guess_the_letter == letter :
            output[position] = letter
    print(output)

    if guess_the_letter not in chosen_word:
        car_parts -= 1
        if car_parts == 0:
            print('Game Over. You have lost all your car parts.')
            end_game = True

    print(f"{' '.join(output)}")
    
    if '_' not in output:
        print('You Have Won!')
        end_game = True

    import hang_art
    print(hang_art.stages[car_parts])