import allure


@allure.step
def test_name_rectangle(create_rectangle):
    assert create_rectangle.name == "Rectangle"


@allure.step
def test_get_area_rectangle(create_rectangle):
    assert create_rectangle.get_area == 50


@allure.step
def test_get_perimetr_rectangle(create_rectangle):
    assert create_rectangle.get_perimetr == 30
