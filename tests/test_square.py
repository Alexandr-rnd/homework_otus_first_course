def test_name_square(create_square):
    assert create_square.name == "Square"


def test_get_area_square(create_square):
    assert create_square.get_area == 100


def test_get_perimetr_square(create_square):
    assert create_square.get_perimetr == 40
