from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def get_perimetr(self):
        return self.side_a * 4

    @property
    def get_area(self):
        return self.side_a * self.side_a
