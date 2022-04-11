def test_name_rectangle(create_rectangle):
    assert create_rectangle.name == "Rectangle"


def test_get_area_rectangle(create_rectangle):
    assert create_rectangle.get_area == 50


def test_get_perimetr_rectangle(create_rectangle):
    assert create_rectangle.get_perimetr == 30
