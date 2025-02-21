def divisible(n):
    for x in range(n + 1):
        if x % 3 == 0 and x % 4 == 0:
            yield x

n = int(input("Enter a number: "))
gen = divisible(n)
for num in gen:
    print(num)