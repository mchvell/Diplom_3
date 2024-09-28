import allure

from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/forgot-password"
        self.email_field = ResetPasswordLocators.EMAIL_FIELD
        self.reset_password_button = ResetPasswordLocators.RESET_PASSWORD_BUTTON
        self.enter_code_field = ResetPasswordLocators.ENTER_CODE_FIELD
        self.password_field = ResetPasswordLocators.PASSWORD_FIELD
        self.hide_password_button = ResetPasswordLocators.HIDE_PASSWORD_BUTTON
        self.password_field_hidden = ResetPasswordLocators.PASSWORD_FIELD_HIDDEN
        self.password_field_shown = ResetPasswordLocators.PASSWORD_FIELD_SHOWN

    @allure.step("Заполнить поле email")
    def fill_email_field_form(self, email):
        locator = self.find_element(self.email_field, 15)
        locator.click()
        locator.send_keys(email)
        return self

    @allure.step("Нажать войти")
    def click_enter_button(self):
        self.find_element(self.reset_password_button, 15).click()

    @allure.step("Получить текст поля с кодом")
    def get_enter_code_text(self):
        locator = self.find_element(self.enter_code_field, 15)
        return locator.text

    @allure.step("Заполнить поле пароль")
    def fill_password_filed(self, password):
        locator = self.find_element(self.password_field, 15)
        locator.click()
        locator.send_keys(password)
        return self

    @allure.step("Раскрыть/скрыть пароль")
    def click_on_hide_password_button(self):
        self.find_element(self.hide_password_button, 15).click()

    @allure.step("Получить состояние поле пароль")
    def get_password_field_state(self):
        locator = self.find_element(self.password_field_shown, 15)
        return locator.get_attribute('class')
