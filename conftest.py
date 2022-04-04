# import pytest
# from src.Triangle import Triangle
# from src.Square import Square
# from src.Rectangle import Rectangle
# from src.Circle import Circle
# from src.Figure import Figure
# #
# def create_correct_figure():
#     triangle = Triangle(10,15,20)
#     square = Square(30)
#     circle = Circle(5)
#     rectangle = Rectangle(10,20)
#     return triangle, square, circle, rectangle
#
# def delete_correct_figure():
#     triangle = None
#     square = None
#     circle = None
#     rectangle = None
#     print("was deleted")
#     return triangle, square, circle, rectangle
#
#
# @pytest.fixture()
# def create_and_clear_figure():
#     create = create_correct_figure()
#     yield create
#     delete_correct_figure()
#
#
