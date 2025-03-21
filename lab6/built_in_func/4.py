import time
import math

number = float(input("Enter the number: "))
milliseconds = float(input("Enter the milliseconds: "))

time.sleep(milliseconds / 1000)
square_root = math.sqrt(number)
print(f"Square root of {number} after {milliseconds} miliseconds is {square_root}")