from inheritance.shapes import Circle, Rectangle, Square


class TestDecoratorsAsFunctions:

    def test_circle(self):
        circle = Circle(10)

        assert 314.1592653589793 == circle.get_area()
        assert 62.83185307179586 == circle.get_perimeter()
        assert '{"radius": 10}' == circle.to_json()

    def test_rectangle(self):
        rectangle = Rectangle(10, 5)

        assert 50 == rectangle.get_area()
        assert 30 == rectangle.get_perimeter()
        assert '{"width": 5, "length": 10}' == rectangle.to_json()

    def test_square(self):
        square = Square(10)

        assert 100 == square.get_area()
        assert 40 == square.get_perimeter()
        assert '{"width": 10, "length": 10}' == square.to_json()




