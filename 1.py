import re

text_to_match = input("Enter your string: ")
pattern = re.compile(r'^ab*$')
result = pattern.fullmatch(text_to_match)
if result:
    print("Match!")
else:
    print("No match!")