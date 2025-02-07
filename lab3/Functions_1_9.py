import math

def volume(radius):
    return (4/3) * math.pi * radius**3

sphere_radius = float(input())
print(f"{volume(sphere_radius):.2f}")