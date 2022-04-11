from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def get_perimetr(self):
        pir = round(pi * 2 * self.side_a, 2)
        return pir

    @property
    def get_area(self):
        return round(pi * self.side_a ** 2, 2)
