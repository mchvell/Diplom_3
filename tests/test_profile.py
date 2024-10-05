import pytest
import allure

from pages.nav_bar import NavBarHelper
from pages.main_page import MainPageHelper
from pages.profile_page import ProfilePageHelper


class TestProfile:
    @allure.title("Проверяем, что при переходе в ЛК без авторизации отображается страница логина")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_profile_click_on_lk(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("lk")
        nav_bar.wait_for_url("/login")
        assert "/login" in nav_bar.get_current_url()

    @allure.title("Проверяем, что после логаута отображается страница логина")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_profile_logout(self, browser, authorization):
        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("lk")

        profile_page = ProfilePageHelper(browser)

        profile_page.click_on_exit_button()
        profile_page.wait_for_url("/login")

        assert "/login" in profile_page.get_current_url()

    @allure.title("Проверяем, что после нажатия на историю заказов осуществляется валидный переход")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_profile_go_to_order_feed(self, browser, authorization):
        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("lk")

        profile_page = ProfilePageHelper(browser)

        profile_page.click_on_order_history()
        profile_page.wait_for_url("/account/order-history")
        assert "/account/order-history" in profile_page.get_current_url()
