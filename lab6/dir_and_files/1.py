import os

def list_dir_and_func(path):
    if not os.path.exists(path):
        print("Path doesn't exist")
        return
    all_items = os.listdir(path)
    directories = [element for element in all_items if os.path.isdir(os.path.join(path, element))]
    files = [element for element in all_items if os.path.isfile(os.path.join(path, element))]

    print("Directories", directories)
    print("Files", files)
    print("All items", all_items)

list_dir_and_func(r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files")