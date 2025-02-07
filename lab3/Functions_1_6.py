def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

sentence = str(input())
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)