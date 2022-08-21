import allure


@allure.step
def test_add_area(create_triangle, create_circle):
    assert create_triangle.add_area(create_circle) == 324.99


@allure.step
def test_add_area1(create_rectangle, create_square):
    assert create_square.add_area(create_square) == 200


@allure.step
def test_add_area2(create_triangle, create_rectangle):
    assert create_triangle.add_area(create_rectangle) == 60.83


@allure.step
def test_add_area3(create_circle, create_square):
    assert create_square.add_area(create_circle) == 414.16


@allure.step
def test_add_incorrect_area(create_square):
    test_item = "тест"
    assert create_square.add_area(test_item) == "ValueError: Incorrect class"
