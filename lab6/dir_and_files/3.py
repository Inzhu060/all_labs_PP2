import os

def find_path(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("File:", os.path.basename(path))
    else:
        print("Path doesn't exist")

find_path(r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files")