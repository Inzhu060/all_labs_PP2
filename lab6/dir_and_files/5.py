import os

list_to_write = ["one", "two", "three", "four", "five"]
new_file = r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files\new_file.txt" 
with open(new_file, "w") as file:
    for item in list_to_write:
        file.write(item + '\n')