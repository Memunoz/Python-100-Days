import random
from art_hangman import logo, stages, animals

chosen_word = random.choice(animals)

display = []
word_length = len(chosen_word)
chosen_list = list(chosen_word)

for _ in range(word_length):
    display += "_"
lives = 6
print(logo)
print(stages[lives])
print(display)
while display != chosen_list:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_list:
        lives -= 1
        print(stages[lives])
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if "_" not in display:
        print('Congratulations! You won!!')
        break
    if lives <= 0:
        print('You lost!')
        break
    print(f"Vidas {lives}♥")
    print(display)
