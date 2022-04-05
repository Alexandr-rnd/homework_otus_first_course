from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Задан не существующий треугольник!")
        else:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c

    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def get_area(self):
        HP = (self.side_a + self.side_b + self.side_c) / 2  # вычисляем полу периметр
        return round(sqrt(HP * (HP - self.side_a) * (HP - self.side_b) * (HP - self.side_c)), 2)
