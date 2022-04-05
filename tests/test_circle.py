def test_name_circle(create_circle):
    assert create_circle.name == "Circle"


def test_get_area_circ(create_circle):
    assert create_circle.get_area == 314.16


def test_get_perimetr_circ(create_circle):
    assert create_circle.get_perimetr == 62.83
