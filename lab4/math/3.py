import math

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the length of the side: "))
area = (sides * length**2) / (4 * math.tan(math.pi / sides))
print("area:", round(area))