import allure
import pytest

from pages.order_feed_page import OrderFeedHelper
from pages.profile_page import ProfilePageHelper
from pages.nav_bar import NavBarHelper
from pages.main_page import MainPageHelper


class TestOrderFeed:
    @allure.title("Проверка открытия модального окна с заказом")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_order_feed_modal_has_opened(self, browser):
        order_feed_page = OrderFeedHelper(browser)
        order_feed_page.go_to_site()
        order_feed_page.click_on_order(order_index=1)
        assert order_feed_page.is_modal_window_opened() is True

    @allure.title("Проверка, что созданный заказ содержится в ленте заказов, и в истории заказов")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_order_history_contains_in_order_feed(self, browser, authorization, create_burger):
        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("order_feed")

        orders = OrderFeedHelper(browser)
        all_orders = orders.get_orders_list()

        nav_bar.switch_tab("lk")
        profile = ProfilePageHelper(browser)
        profile.click_on_order_history()
        # получаем список всех заказов юзера
        user_orders = profile.get_attribute_order_feed()

        # хотя бы один заказ найден в списке всех заказов
        assert any(order in all_orders for order in user_orders)

    @allure.title("Проверка, что созданный заказ увеличивает количество заказов")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_increase_order_counter_for_all_time(self, browser, authorization, create_burger):
        order_no = create_burger

        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("order_feed")

        order_feed = OrderFeedHelper(browser)
        total_no = order_feed.get_all_order_numbers()
        # больше или равно, тк другие пользователи тоже могут оформить заказы
        assert total_no >= order_no

    @allure.title("Проверка, что созданный заказ увеличивает количество заказов сегодня")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_increase_order_counter_for_today(self, browser, authorization):
        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("order_feed")

        order_feed = OrderFeedHelper(browser)
        before_order = order_feed.get_today_order_numbers()

        nav_bar.switch_tab("main")

        main_page = MainPageHelper(browser)
        main_page.drag_and_drop_item(type="bread", name="fluorescent")

        main_page.click_on_order_button()
        main_page.close_modal_order_window()

        nav_bar.switch_tab("order_feed")
        after_order = order_feed.get_today_order_numbers()

        assert before_order < after_order

    @allure.title("Проверка, что созданный заказ находится готовится")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_new_order_contains_in_progress_list(self, browser, authorization, create_burger):
        order_no = create_burger
        nav_bar = NavBarHelper(browser)
        nav_bar.switch_tab("order_feed")

        order_feed = OrderFeedHelper(browser)
        order_in_process = order_feed.get_orders_in_process()
        assert order_no == order_in_process
