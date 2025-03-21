import math

numbers = list(map(int, input("Enter numbers: ").split()))
result = math.prod(numbers)
print(result)