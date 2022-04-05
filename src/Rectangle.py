from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_perimetr(self):
        pir = self.side_a * 2 + self.side_b * 2
        return pir

    @property
    def get_area(self):
        S = self.side_a * self.side_b
        return S
