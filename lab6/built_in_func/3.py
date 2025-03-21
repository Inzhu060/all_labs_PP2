def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Enter the word: ")
if is_palindrome(word):
    print("It is a palindrome!")
else:
    print("It's not a palindrome!")