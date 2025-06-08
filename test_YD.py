import pytest
import requests
from unittest import mock

# Мокируем import requests в yandex_disk
with mock.patch.dict('sys.modules', requests=requests):
    from yandex_disk import YD


@pytest.fixture
def yd_client():
    return YD(token="test_token")


@pytest.mark.parametrize("status_code, expected_result", [
    (201, True),   # Успешное создание
    (200, True),   # Папка уже существует
    (409, True),   # Конфликт
    (401, False),  # Неверный токен
    (400, False),  # Некорректный запрос
    (500, False),  # Ошибка сервера
])
def test_create_folder(yd_client, status_code, expected_result, requests_mock):
    folder_name = "test_folder"

    # Мокируем ответ ЯД
    requests_mock.put(
        "https://cloud-api.yandex.net/v1/disk/resources", 
        status_code=status_code
    )

    result = yd_client.create_folder(folder_name)

    assert result == expected_result