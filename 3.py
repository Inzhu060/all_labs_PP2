import re

text_to_match = input("Enter the string: ")
pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
result = pattern.findall(text_to_match)
print(result)