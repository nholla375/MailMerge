with open("Input/Letters/starting_letter.txt") as starting_letter:
    base = starting_letter.read()
    with open("Input/Names/invited_names.txt") as names:
        name_list = names.readlines()
        for name in name_list:
            modded_letter = base.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as letter:
                letter.write(modded_letter)

# name.strip() required bc names.readlines() adds a /n to the end of every line/name.