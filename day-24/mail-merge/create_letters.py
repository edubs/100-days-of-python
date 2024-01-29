with open("./input/names/invite_names.txt") as names_file:
    names_list = names_file.read().splitlines()

for name in names_list:
    stripped_name = name.strip()
    with open("./input/letters/starting_letter.txt") as letter_base:
        letter_contents = letter_base.read()
        letter_contents = letter_contents.replace("[name]", stripped_name)
        stripped_name = name.replace(" ", "_")

    letter_name = f"./output/readytosend/letter_for_{stripped_name}.txt"
    with open(letter_name, mode="a") as new_letter:
        new_letter.write(letter_contents)
