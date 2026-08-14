from pathlib import Path

PLACEHOLDER = "[name]"

base_path = Path(__file__).parent

names_file_path = base_path / "Input" / "Names" / "invited_names.txt"
with open(names_file_path) as names_file:
    names = names_file.readlines()

letter_file_path = base_path / "Input" / "Letters" / "starting_letter.txt"
with open(letter_file_path) as letter_file:
    letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    output_file_path = base_path / "Output" / "ReadyToSend" / f"letter_for_{stripped_name}.txt"

    with open(output_file_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)