import re

def snake_to_camel(text):
    words = text.split("_")
    s_words = words[0] + ''.join(word.capitalize() for word in words[1:])
    return s_words

text = input("Enter the string: ")
print(snake_to_camel(text))