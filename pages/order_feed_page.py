import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as orders
from selenium.webdriver.support.ui import WebDriverWait
import re


class OrderFeedHelper(BasePage):
    WAIT_TIME = 15

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/feed"
        self.modal_window = orders.MODAL_WINDOW_OPENED  # Avoid double declaration
        self.orders_in_process = orders.ORDERS_IN_PROCESS
        self.orders_ready = orders.ORDERS_READY
        self.orders_list = orders.ORDER_FEED_LIST
        self.all_orders = orders.ORDER_COUNTER_FOR_ALL_TIME
        self.today_orders = orders.ORDER_COUNTER_FOR_TODAY

    @allure.step("Нажать на заказ")
    def click_on_order(self, order_index):
        locator = orders.get_order_locator(index=order_index)
        self.find_element(locator).click()

    @allure.step("Проверка открытия модального окна")
    def is_modal_window_opened(self):
        modal_class = self.find_element(self.modal_window, self.WAIT_TIME).get_attribute('class')
        return "opened" in modal_class

    @allure.step("Получить список заказов на странице")
    def get_orders_list(self):
        return [element.text for element in self.find_elements(self.orders_list)]

    @allure.step("Получить значение заказов из каунтера")
    def get_all_order_numbers(self):
        number = self.find_element(self.all_orders, self.WAIT_TIME).text
        return int(number)

    @allure.step("Получить значение заказов за сегодн из каунтера")
    def get_today_order_numbers(self):
        number = self.find_element(self.today_orders, self.WAIT_TIME).text
        return int(number)

    @allure.step("Получить значение заказов в процессе")
    def get_orders_in_process(self):
        order_text = WebDriverWait(self.driver, self.WAIT_TIME).until(
            lambda driver: re.search(r'\d+', self.find_element(self.orders_in_process).text)
        ).group()

        return int(order_text)
