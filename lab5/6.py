import re

text_to_match = input("Enter the string: ")
pattern = r'[ ,.]'
replace_the_sequence = re.sub(pattern, ":", text_to_match)
print(replace_the_sequence)