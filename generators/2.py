def even_numbers(n):
    for x in range(n + 1):
        if x % 2 == 0:
            yield x

n = int(input("Enter a number: "))
gen = even_numbers(n)
print(", ".join(map(str, gen)))