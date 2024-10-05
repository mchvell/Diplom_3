from selenium.webdriver.common.by import By


class NavBarLocators:
    NAVBAR_TABS = {
        "constructor": (By.XPATH, "//p[text()='Конструктор']"),
        "order_feed": (By.XPATH, "//p[text()='Лента Заказов']"),
        "main": (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"),
        "lk": (By.XPATH, "//p[text()='Личный Кабинет']")
    }