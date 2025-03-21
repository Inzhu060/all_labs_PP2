import os

file_path = r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files\info.txt" 
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File is removed")
    else:
        print("There is no access to remove")
else:
    print("File doesn't exist")