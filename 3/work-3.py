from math import sqrt, pi

# Base class.
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def compare_area(self, other):
        pass
    
    def compare_perimeter(self, other):
        pass

# Square
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def compare_area(self, other):
        return self._compare(self.area(), other.area())
    
    def compare_perimeter(self, other):
        return self._compare(self.perimeter(), other.perimeter())
    
    def _compare(self, value1, value2):
        if value1 > value2:
            return True
        else:
            return False

# Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def compare_area(self, other):
        return self._compare(self.area(), other.area())
    
    def compare_perimeter(self, other):
        return self._compare(self.perimeter(), other.perimeter())
    
    def _compare(self, value1, value2):
        if value1 > value2:
            return True
        else:
            return False

# Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula to calculate the area.
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def compare_area(self, other):
        return self._compare(self.area(), other.area())
    
    def compare_perimeter(self, other):
        return self._compare(self.perimeter(), other.perimeter())
    
    def _compare(self, value1, value2):
        if value1 > value2:
            return True
        else:
            return False

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    
    def compare_area(self, other):
        return self._compare(self.area(), other.area())
    
    def compare_perimeter(self, other):
        return self._compare(self.perimeter(), other.perimeter())
    
    def _compare(self, value1, value2):
        if value1 > value2:
            return True
        else:
            return False

# Example
square = Square(4)
rectangle = Rectangle(3, 4)
triangle = Triangle(3, 4, 5)
circle = Circle(5)

print("Square area:", square.area())
print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())
print("Circle area:", circle.area())

print("Square perimeter:", square.perimeter())
print("Rectangle perimeter:", rectangle.perimeter())
print("Triangle perimeter:", triangle.perimeter())
print("Circle perimeter:", circle.perimeter())

print("Square vs Circle area:", square.compare_area(circle))
print("Square vs Circle perimeter:", square.compare_perimeter(circle))