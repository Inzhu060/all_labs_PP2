import os

file_name = r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files\info.txt" 
count = 0
with open(file_name, "r") as file:
    for line in file:
        count += 1
print(count)