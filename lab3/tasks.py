def histogram(lst):
    for num in lst:
        print("*" * num)

def is_palindrome(word):
    word = ''.join(filter(str.isalnum, word)).lower()
    return word == word[::-1]

def sphere_volume(radius):
    import math
    return (4/3) * math.pi * radius**3

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False
