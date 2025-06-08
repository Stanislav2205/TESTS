import pytest
# тест для задания "Проверка возраста"
def check_age(age: int):
    if age >= 18:
        return 'Доступ разрешён'
    else:
        return 'Доступ запрещён'

@pytest.mark.parametrize("age, expected", [
    (10, 'Доступ запрещён'),
    (17, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (25, 'Доступ разрешён'),
])
def test_check_age(age, expected):
    assert check_age(age) == expected

# тест для задания "Проверка логина и пароля"
def check_auth(login: str, password: str):
    if login == 'admin' and password == 'password':
        return 'Добро пожаловать'
    else:
        return 'Доступ ограничен'

@pytest.mark.parametrize("login, password, expected", [
    ('user', 'password', 'Доступ ограничен'),
    ('admin', '123', 'Доступ ограничен'),
    ('admin', 'password', 'Добро пожаловать'),
    ('ADMIN', 'password', 'Доступ ограничен'),
    ('admin', 'Password', 'Доступ ограничен'),
])
def test_check_auth(login, password, expected):
    assert check_auth(login, password) == expected

# тест для задания "Стоимость доставки"
def get_cost(weight: int):
    if weight <= 10:
        return 'Стоимость доставки: 200 руб.'
    else:
        return 'Стоимость доставки: 500 руб.'

@pytest.mark.parametrize("weight, expected_price", [
    (0, '200'),
    (10, '200'),
    (11, '500'),
    (50, '500'),
])
def test_get_cost(weight, expected_price):
    result = get_cost(weight)
    assert expected_price in result


