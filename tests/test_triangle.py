import pytest
from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle


def test_name_trio(create_triangle):
    assert create_triangle.name == "Triangle"


def test_get_area_trio(create_triangle):
    assert create_triangle.get_area == 10.83


def test_get_perimetr_trio(create_triangle):
    assert create_triangle.get_perimetr == 15


def test_incorrect_area_trio():
    with pytest.raises(ValueError) as context:
        t = Triangle(1, 1, 5)
    assert 'Задан не существующий треугольник!' in str(context)
