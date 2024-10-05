from selenium.webdriver.common.by import By


class OrderFeedLocators:
    @staticmethod
    def get_order_locator(index: int):
        xpath = f"//li[contains(@class, 'OrderHistory_listItem')][{index}]"
        return By.XPATH, xpath

    MODAL_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]")

    ORDERS_IN_PROCESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text')]")

    ORDERS_READY = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li")

    MODAL_WINDOW_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened') and contains(@class, 'Modal_modal')]")

    ORDER_FEED_LIST = (By.XPATH, "//p[contains(@class, 'text text_type_digits') and contains(text(), '#')]")

    ORDER_COUNTER_FOR_ALL_TIME = (By.XPATH, "//div[p[contains(text(), 'Выполнено за все время:')]]/p[contains(@class, 'OrderFeed_number')]")

    ORDER_COUNTER_FOR_TODAY = (By.XPATH, "//div[p[contains(text(), 'Выполнено за сегодня:')]]/p[contains(@class, 'OrderFeed_number')]")