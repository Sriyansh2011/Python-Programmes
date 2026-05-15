from abc import ABC, abstractmethod
3
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Polygon):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

print("Choose Polygon")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))

    obj = Rectangle(l, b)
    print("Area of Rectangle =", obj.area())

elif choice == 2:
    s = float(input("Enter side: "))

    obj = Square(s)
    print("Area of Square =", obj.area())

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    obj = Triangle(base, height)
    print("Area of Triangle =", obj.area())

else:
    print("Invalid Choice")