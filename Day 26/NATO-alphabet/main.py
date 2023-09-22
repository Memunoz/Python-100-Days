import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {n.letter: n.code for (k, n) in df.iterrows()}
# nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generator():
    word = input("insert a word: ").upper()
    try:
        spell = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Only letters")
        generator()
    else:
        print(spell)


generator()
