import math

from faker import Faker

from inheritance.shapes import Circle, Rectangle, Square


class TestDecoratorsAsFunctions:

    def test_circle(self):
        faker = Faker()
        radius = faker.pyfloat()

        circle = Circle(radius)

        expected_area = math.pi * pow(radius, 2)
        expected_perimeter = math.pi * radius * 2

        assert expected_area == circle.get_area()
        assert expected_perimeter == circle.get_perimeter()
        assert f'{{"radius": {radius}}}' == circle.to_json()

    def test_rectangle(self):
        faker = Faker()
        width = faker.pyint()
        length = faker.pyint()

        rectangle = Rectangle(length, width)

        expected_area = width * length
        expected_perimeter = width * 2 + length * 2

        assert expected_area == rectangle.get_area()
        assert expected_perimeter == rectangle.get_perimeter()
        assert f'{{"width": {width}, "length": {length}}}' == rectangle.to_json()

    def test_square(self):
        faker = Faker()
        side = faker.pyint()
        square = Square(side)

        expected_area = side * side
        expected_perimeter = side * 4

        assert expected_area == square.get_area()
        assert expected_perimeter == square.get_perimeter()
        assert f'{{"width": {side}, "length": {side}}}' == square.to_json()




