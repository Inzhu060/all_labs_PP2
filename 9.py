import re

text = input("Enterthe string: ")
pattern = r'(?<!^)(?=[A-Z])'
result = re.sub(pattern, " ", text)
print(result)