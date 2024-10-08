import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as orders
import re


class OrderFeedHelper(BasePage):
    WAIT_TIME = 15
    WAIT_TIME_LONG = 40

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/feed"
        self.modal_window = orders.MODAL_WINDOW_OPENED
        self.orders_in_process = orders.ORDERS_IN_PROCESS
        self.orders_ready = orders.ORDERS_READY
        self.orders_list = orders.ORDER_FEED_LIST
        self.all_orders = orders.ORDER_COUNTER_FOR_ALL_TIME
        self.today_orders = orders.ORDER_COUNTER_FOR_TODAY

    @allure.step("Нажать на заказ")
    def click_on_order(self, order_index):
        locator = orders.get_order_locator(index=order_index)
        self.click_element(locator)

    @allure.step("Проверка открытия модального окна")
    def is_modal_window_opened(self):
        modal_class = self.get_element_attribute(self.modal_window, 'class', self.WAIT_TIME)
        return "opened" in modal_class

    @allure.step("Получить список заказов на странице")
    def get_orders_list(self):
        return [element.text for element in self.find_elements(self.orders_list, self.WAIT_TIME)]

    @allure.step("Получить значение заказов из каунтера")
    def get_all_order_numbers(self):
        number = self.get_element_text(self.all_orders, self.WAIT_TIME)
        return int(number)

    @allure.step("Получить значение заказов за сегодня из каунтера")
    def get_today_order_numbers(self):
        number = self.get_element_text(self.today_orders, self.WAIT_TIME_LONG)
        return int(number)

    # Пробовал упростить реализацию, но постоянно ломается(
    @allure.step("Получить количество заказов в процессе")
    def get_orders_in_process(self):
        while True:
            try:
                order_text = self.get_element_text(self.orders_in_process, self.WAIT_TIME_LONG)

                match = re.search(r'\d+', order_text)

                if match:
                    return int(match.group())

            except Exception as e:
                pass