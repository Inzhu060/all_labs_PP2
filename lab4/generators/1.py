def squares(n):
    for x in range(n + 1):
        yield x ** 2

n = int(input())
gen = squares(n)
for num in gen:
    print(num)