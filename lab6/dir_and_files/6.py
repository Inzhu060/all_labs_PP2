import string

for letter in string.ascii_uppercase:
    new_file = f"{letter}.txt"
    with open(f"{letter}.txt", "w") as file:
        file.write(new_file)