import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    @allure.step("Найти элемент")
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Найти элементы")
    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Ожидать видимость элемента")
    def wait_for_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )

    @allure.step("Ожидать, что элемент станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )

    @allure.step("Кликнуть элемент")
    def click_element(self, locator, time=15):
        element = self.wait_for_element_to_be_clickable(locator, time)
        element.click()

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator, time=15):
        element = self.wait_for_element(locator, time)
        return element.text

    @allure.step("Получить атрибут элемента")
    def get_element_attribute(self, locator, attribute, time=15):
        element = self.wait_for_element(locator, time)
        return element.get_attribute(attribute)

    @allure.step("Перейти на сайт")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("Дождаться URL")
    def wait_for_url(self, url_substring, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.url_contains(url_substring),
            message=f"URL не содержит '{url_substring}' спустя {time} секунд"
        )

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать, что текст элемента изменится")
    def wait_for_element_text_to_change(self, locator, old_text, time=15):
        return WebDriverWait(self.driver, time).until(
            lambda driver: self.find_element(locator, time).text.strip() != old_text,
            message=f"Текст элемента {locator} не изменился"
        )

    @allure.step("Ожидать, что элемент отображён")
    def wait_for_element_to_be_displayed(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            lambda driver: self.find_element(locator, time).is_displayed(),
            message=f"Элемент {locator} не отображается"
        )

    @allure.step("Заполнить поле")
    def fill_field(self, locator, value, time=15):
        element = self.wait_for_element(locator, time)
        element.click()  # Кликаем перед вводом текста
        element.send_keys(value)
        return self
