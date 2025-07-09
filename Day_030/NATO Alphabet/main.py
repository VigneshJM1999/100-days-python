import pandas

def phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [nato_alphabets[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only alphabets are allowed.")
        phonetic()
    else:
        print(phonetic_list)


data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}

phonetic()
