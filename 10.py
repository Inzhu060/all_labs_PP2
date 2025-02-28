import re

text = input("Enterthe string: ")
pattern = r'(?<!^)(?=[A-Z])'
split_word = re.sub(pattern, "_", text).lower()
print(split_word)