import pytest
import allure

from pages.nav_bar import NavBarHelper
from pages.main_page import MainPageHelper
from pages.auth_page import AuthPageHelper


class TestNavBar:

    @allure.description("Проверяем, что при переходе на главную отображается конструктор на вкладе 'Булки'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_open_constructor(self, browser):
        auth_page = AuthPageHelper(browser)
        auth_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("constructor")

        main_page = MainPageHelper(browser)
        constructor_tab = main_page.get_tab_header_text("bread")
        assert constructor_tab == "Булки"

    @allure.description("Проверяем переход на вкладку 'Лента заказов'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_order_feed(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("order_feed")
        url = browser.current_url
        assert "/feed" in url
