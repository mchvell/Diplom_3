import allure
from faker import Faker
import requests


class UserData:
    auth_url = "https://stellarburgers.nomoreparties.site/api/auth/register"
    delete_url = "https://stellarburgers.nomoreparties.site/api/auth/user"

    @staticmethod
    def generate_name():
        faker = Faker('ru_RU')
        return faker.name()

    @staticmethod
    def generate_email():
        faker = Faker('ru_RU')
        return faker.email()

    @staticmethod
    def generate_password():
        faker = Faker('ru_RU')
        return str(faker.password())

    @staticmethod
    def generate_user_credentials():
        name = UserData.generate_name()
        email = UserData.generate_email()
        password = UserData.generate_password()
        return {
            "name": name,
            "email": email,
            "password": password
        }

    @allure.step("Создаем нового пользователя")
    def create_user(self):
        user_credentials = self.generate_user_credentials()
        response = requests.post(url=self.auth_url, data=user_credentials)
        jwt = response.json().get("accessToken")
        return user_credentials, jwt

    @allure.step("Удаляем созданного пользователя")
    def delete_user(self, jwt):
        headers = {
            "Authorization": jwt
        }
        response = requests.delete(url=self.delete_url, headers=headers)
        response.raise_for_status()
