import pandas
from pathlib import Path

file_path = Path(__file__).parent / "nato_phonetic_alphabet.csv"

file_read = pandas.read_csv(file_path)

phonetic_dict= {row.letter:row.code for (index, row) in file_read.iterrows()}
print(phonetic_dict)

valid = True
while valid:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        valid = False
    except KeyError:
        print("Sorry, only letters in the name please!")
        valid = True
    else:
         print(output_list)
   

