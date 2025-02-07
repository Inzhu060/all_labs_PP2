import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
point1 = Point(4, 5)
point1.show()

point2 = Point(6, 7)
print("Distance: ", point1.dist(point2))

point1.move(11, 12)
point1.show()
