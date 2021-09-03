import math


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    circles_list = []

    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)

    def add_circles(self, other_circle):
        area = self.get_area() + other_circle.get_area()
        print(f"The area of the 2 circles together is: {area}")

    def bigger_circle(self, other_circle):
        if self.get_area() > other_circle.get_area():
            print(f"The first circle is bigger, with an area of {self.get_area()}")
        else:
            print(f"The second circle is bigger, with an area of {other_circle.get_area()}")

    def is_equal(self, other_circle):
        if self.get_area() == other_circle.get_area():
            print("Both circles are equal")
        else:
            print("The circles are not equal")

    def add_to_list(self):
        self.circles_list.append(self)
        self.circles_list.sort(key=Circle.get_area)
        print("The order of the Circles in the list in ascendant order is: ")
        for item in self.circles_list:
            print(item.get_area())


circle1 = Circle(5)
circle2 = Circle(10)
print(circle1.get_area())
circle1.add_circles(circle2)
circle1.bigger_circle(circle2)
circle1.is_equal(circle2)
circle1.add_to_list()
circle2.add_to_list()
