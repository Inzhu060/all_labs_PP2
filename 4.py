import re

text_to_match = input("Enter the string: ")
pattern = re.compile(r'\b[A-Z][a-z]+\b')
match = pattern.findall(text_to_match)
print(match)