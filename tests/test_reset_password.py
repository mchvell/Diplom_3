import pytest
import allure

from pages.auth_page import AuthPageHelper
from pages.reset_password_page import ResetPasswordHelper


class TestResetPassword:
    @allure.title("Проверяем переход на правильную страницу после нажатия 'Забыл пароль'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_reset_password_link(self, browser):
        auth_page = AuthPageHelper(driver=browser)
        auth_page.go_to_site()
        auth_page.click_link("reset_password")
        auth_page.wait_for_url("/forgot-password")
        assert "/forgot-password" in auth_page.get_current_url()

    @allure.title("Проверяем, что после нажатия забыл пароль и ввода почты отображается новая форма")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_fill_reset_password(self, browser):
        reset_password_page = ResetPasswordHelper(driver=browser)
        reset_password_page.go_to_site()
        reset_password_page.fill_email_field("gubanov12qa@yandex.ru")
        reset_password_page.click_on_restore_password_button()
        text = reset_password_page.get_enter_code_text()
        assert text == "Введите код из письма"

    @allure.title("Проверяем, что поле пароль можны сделать видимым")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_hide_password_button(self, browser):
        reset_password_page = ResetPasswordHelper(driver=browser)
        reset_password_page.go_to_site()
        reset_password_page.fill_email_field("gubanov12qa@yandex.ru")
        reset_password_page.click_on_restore_password_button()
        reset_password_page.fill_password("12345")
        reset_password_page.click_on_hide_password_button()
        active_state = reset_password_page.get_password_field_state()
        assert 'input_status_active' in active_state
