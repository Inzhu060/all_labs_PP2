import os 

target_folder = r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab6\dir_and_files"  
os.chdir(target_folder)  

file_name ='test.txt'
with open(file_name, 'w') as file:
    file.write("Hello World")

print(os.access(file_name, os.F_OK)) 
print(os.access(file_name, os.R_OK)) 
print(os.access(file_name, os.W_OK)) 
print(os.access(file_name, os.X_OK)) 