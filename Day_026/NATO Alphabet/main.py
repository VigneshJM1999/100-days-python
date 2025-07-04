import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_list = [nato_alphabets[letter] for letter in user_input if letter in nato_alphabets]
print(phonetic_list)
