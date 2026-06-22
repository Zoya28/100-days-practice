with open("./Input/Names/invited_names.txt", "r") as data:
    names = data.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        letter = letter_content.replace("[name]", name)
        with open(f"Output/ReadyToSend/Letter_for_{name}.txt", "w") as complete_letters:
            complete_letters.write(letter)
