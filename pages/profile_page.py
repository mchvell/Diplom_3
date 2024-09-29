import allure


from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as p


class ProfilePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/account/profile"
        self.exit_button = p.EXIT_BUTTON
        self.order_feed = p.ORDER_FEED_LINK
        self.order_ids = p.ORDERS_IDS

    @allure.step("Выйти из профиля")
    def click_on_exit_button(self):
        return self.click_element(self.exit_button)

    @allure.step("Перейти в историю заказов")
    def click_on_order_history(self):
        return self.click_element(self.order_feed)

    @allure.step("Получить список заказов пользователя")
    def get_attribute_order_feed(self):
        elements = self.find_elements(self.order_ids, 15)
        return [element.text for element in elements]
