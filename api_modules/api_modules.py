import allure
import requests
from data.user_generator import UserData


class UserAPI:
    auth_url = "https://stellarburgers.nomoreparties.site/api/auth/register"
    delete_url = "https://stellarburgers.nomoreparties.site/api/auth/user"

    @allure.step("Создаем нового пользователя")
    def create_user(self):
        user_credentials = UserData.generate_user_credentials()  # Генерируем учетные данные
        response = requests.post(url=self.auth_url, data=user_credentials)
        response.raise_for_status()  # Проверяем успешность запроса
        jwt = response.json().get("accessToken")
        return user_credentials, jwt

    @allure.step("Удаляем созданного пользователя")
    def delete_user(self, jwt):
        headers = {
            "Authorization": jwt
        }
        response = requests.delete(url=self.delete_url, headers=headers)
        response.raise_for_status()