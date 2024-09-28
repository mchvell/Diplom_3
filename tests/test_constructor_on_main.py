import allure
import pytest


from pages.main_page import MainPageHelper


class TestMainPageConstructor:
    @allure.description("Проверяем, что при нажатии на игридиент открывается модальное окно")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_ingredient(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        main_page.click_on_sauce()
        assert main_page.is_modal_window_visible() is True

    @allure.description("Проверяем, что при нажатии на игридиент открывается модальное окно и закрываем его")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_ingredient_and_close_modal(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        main_page.click_on_sauce()
        main_page.close_modal_window()
        assert main_page.is_modal_window_hidden() is True

    @allure.description("Проверяем, что при d&d меняется каунтер соуса")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_drag_and_drop_sauce(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()

        main_page.drag_and_drop_item(type="sauce", name="spice_x")
        sauce_counter = main_page.get_sauce_counter_value()
        assert "1" in sauce_counter

    @allure.description("Проверяем, авторизованный юзер может создрать заказ")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_create_order(self, browser, authorization):
        main_page = MainPageHelper(browser)

        main_page.drag_and_drop_item(type="sauce", name="spice_x")
        main_page.drag_and_drop_item(type="bread", name="fluorescent")

        main_page.set_tab("topping")
        main_page.drag_and_drop_item(type="filling", name="protostomia")

        main_page.click_on_order_button()

        assert main_page.is_modal_window_visible() is True
