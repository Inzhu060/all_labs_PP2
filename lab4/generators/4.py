def squares(a, b):
    for x in range(a, b + 1):
        yield x ** 2

a = int(input("Enter: "))
b = int(input("Enter: "))
gen = squares(a, b)
for num in gen:
    print(num)