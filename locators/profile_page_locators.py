from selenium.webdriver.common.by import By


class ProfilePageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_FEED_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")
    ORDERS_IDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text text_type_digits-default')]")
