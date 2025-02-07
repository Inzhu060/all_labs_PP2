def is_palindrome(word):
    word = ''.join(filter(str.isalnum, word)).lower()
    return word == word[::-1]

word = input("Enter: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome!")