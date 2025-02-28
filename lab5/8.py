import re

text = input("Enter the string: ")
pattern = r'(?=[A-Z])'
split_word = re.split(pattern, text)
split_word = [word for word in split_word if word]
print(split_word)