import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


@pytest.fixture()
def create_triangle():
    triangle_test = Triangle(side_a=5, side_b=5, side_c=5)
    return triangle_test


@pytest.fixture()
def create_circle():
    circle_test = Circle(side_a=10)
    return circle_test


@pytest.fixture()
def create_rectangle():
    rectangle_test = Rectangle(side_a=5, side_b=10)
    return rectangle_test


@pytest.fixture()
def create_square():
    square_test = Square(side_a=10)
    return square_test
