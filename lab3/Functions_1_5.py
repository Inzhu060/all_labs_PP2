from itertools import permutations

def permutation():
    word = input("Enter word: ")
    perms = permutations(word)
    for perm in perms:
        print("".join(perm))

permutation()