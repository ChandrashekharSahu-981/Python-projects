import pandas
from pathlib import Path

file_path = Path(__file__).parent / "nato_phonetic_alphabet.csv"

file_read = pandas.read_csv(file_path)

#Create a dictionary from the dataframe
phonetic_dict= {row.letter:row.code for (index, row) in file_read.iterrows()}

#Create a list of the phonetic code words from user input
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

