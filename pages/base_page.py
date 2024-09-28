import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    @allure.step("Найти элемент")
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Элемент {locator} не найден")

    @allure.step("Найти элементы")
    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Элемент {locator} не найден")

    @allure.step("Перейти на по урлу")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("Дождаться урла")
    def wait_for_url(self, url_substring, time=15):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url_substring),
                                                      message=f"URL не содержит '{url_substring}' спустя {time} секунд")
