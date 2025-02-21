n = int(input("Enter a number: "))
gen = (x for x in range(n, -1, -1))
print(*gen)