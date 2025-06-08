import requests

class YD:
    def __init__(self, token):
        self.token = token

    def create_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources" 
        headers = {"Authorization": f"OAuth {self.token}"}
        params = {"path": folder_name}
        response = requests.put(url, headers=headers, params=params)

        if response.status_code not in [200, 201, 409]:
            try:
                error_data = response.json()
            except requests.exceptions.JSONDecodeError:
                error_data = {}  #  так как не будет JSON потому что мокируем ответ, добавил использование пустого словаря
            print(f"Ошибка при создании папки: {error_data}")  # выводим информацию об ошибке
            return False
        return True
