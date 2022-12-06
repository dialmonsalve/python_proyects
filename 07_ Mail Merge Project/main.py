PLACEHOLDER = "[name]"

with open("07_ Mail Merge Project/Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open("07_ Mail Merge Project/Input/Letters/starting_letter.txt") as letter_file:
    leter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = leter_content.replace(PLACEHOLDER, stripped_name)
        
        with open(f"07_ Mail Merge Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)
