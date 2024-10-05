import allure

from pages.base_page import BasePage
from locators.auth_page_locators import AuthLocators


class AuthPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/login"
        self.input_locators = AuthLocators.INPUTS
        self.enter_button_locator = AuthLocators.ENTER_BUTTON
        self.link_locators = AuthLocators.LINKS

    @allure.step("Заполнить форму авторизации")
    def fill_auth_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = self.input_locators.get(field)
            self.fill_field(locator, value)
        return self

    @allure.step("Нажать на кнопку входа")
    def click_enter_button(self):
        self.click_element(self.enter_button_locator)

    @allure.step("Нажать на 'Забыл пароль'")
    def click_link(self, link_name):
        link_locator = self.link_locators.get(link_name)
        return  self.click_element(link_locator)

