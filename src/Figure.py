class Figure():

    def add_area(self, figure2):
        if isinstance(figure2, Figure) == True:
            return round(self.get_area + figure2.get_area, 2)
        else:
            return "ValueError: Incorrect class"
