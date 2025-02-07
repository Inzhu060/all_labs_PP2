def Conversion (Fahrenheit):
    return (5 / 9) * (Fahrenheit - 32)

Fahrenheit = float(input("Enter the temperature: "))
Celcius = Conversion(Fahrenheit)
print(f"Temperature in Celcius is {Celcius:.2f}")