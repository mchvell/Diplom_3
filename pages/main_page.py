import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPageHelper(BasePage):
    WAIT_TIME_SHORT = 10
    WAIT_TIME_MEDIUM = 15
    WAIT_TIME_LONG = 60

    def __init__(self, driver):
        super().__init__(driver)
        self.tab_locators = MainPageLocators.TABS
        self.tab_header_locators = MainPageLocators.TABS_HEADERS
        self.sauce = MainPageLocators.SAUCE
        self.close_modal_icon = MainPageLocators.MODAl_WINDOW_CLOSE
        self.modal_state_opened = MainPageLocators.MODAL_WINDOW_OPENED
        self.modal_state_hidden = MainPageLocators.MODAL_WINDOW_HIDDEN
        self.burger_constructor = MainPageLocators.ORDER_CONSTRUCTOR
        self.sauce_counter = MainPageLocators.SAUCE_COUNTER
        self.order_button = MainPageLocators.CREATE_ORDER_BUTTON
        self.order_no = MainPageLocators.ORDER_NUMBER
        self.modal_check_animation = MainPageLocators.MODAL_WINDOW_ORDER_ACCESS
        self.sauces = MainPageLocators.SAUCES
        self.fillings = MainPageLocators.FILLINGS
        self.bread = MainPageLocators.BREAD

    @allure.step("Устанавливает вкладку конструктора")
    def set_tab(self, tab):
        tab_locator = self.tab_locators.get(tab)
        self.click_element(tab_locator, self.WAIT_TIME_SHORT)

    @allure.step("Получает текст вкладки конструктора")
    def get_tab_header_text(self, tab):
        header_locator = self.tab_header_locators.get(tab)
        return self.get_element_text(header_locator, self.WAIT_TIME_SHORT)

    @allure.step("Нажимает на соус")
    def click_on_sauce(self):
        self.click_element(self.sauce, self.WAIT_TIME_MEDIUM)

    @allure.step("Закрывает модальное окно ингридиента")
    def close_modal_window(self):
        self.click_element(self.close_modal_icon, self.WAIT_TIME_MEDIUM)

    @allure.step("Закрывает модальное окно заказа")
    def close_modal_order_window(self):
        while True:
            if self.wait_for_element(self.modal_check_animation, self.WAIT_TIME_MEDIUM):
                try:
                    self.click_element(self.close_modal_icon, self.WAIT_TIME_MEDIUM)
                    break
                except Exception:
                    continue

    @allure.step("Проверяет состояние модального окна на открытость")
    def is_modal_window_visible(self):
        modal_class = self.get_element_attribute(self.modal_state_opened, 'class', self.WAIT_TIME_MEDIUM)
        return "opened" in modal_class

    @allure.step("Проверяет состояние модального окна на закрытость")
    def is_modal_window_hidden(self):
        modal_class = self.get_element_attribute(self.modal_state_hidden, 'class', self.WAIT_TIME_MEDIUM)
        return "opened" not in modal_class

    @allure.step("Получает количество в каунтере для соуса")
    def get_sauce_counter_value(self):
        return self.get_element_text(self.sauce_counter, self.WAIT_TIME_MEDIUM)

    @allure.step("Создает бургер исходя из входных параметров")
    def drag_and_drop_item(self, **kwargs):
        item_type = kwargs.get('type')
        item_name = kwargs.get('name')

        locator_map = {
            "sauce": self.sauces,
            "bread": self.bread,
            "filling": self.fillings
        }

        item_element = locator_map[item_type].get(item_name)
        item_locator = self.find_element(item_element, self.WAIT_TIME_MEDIUM)
        target_element = self.wait_for_element(self.burger_constructor, self.WAIT_TIME_MEDIUM)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(item_locator, target_element).perform()

    @allure.step("Нажимает на кнопку заказать")
    def click_on_order_button(self):
        self.click_element(self.order_button, self.WAIT_TIME_MEDIUM)

    @allure.step("Получает номер заказа")
    def get_order_number(self):
        self.wait_for_element_to_be_displayed(self.order_no, self.WAIT_TIME_MEDIUM)

        order_number_element = self.find_element(self.order_no, self.WAIT_TIME_MEDIUM)
        order_number_text = order_number_element.text.strip()

        order_number = int(order_number_text)
        if order_number == 9999:
            self.wait_for_element_text_to_change(self.order_no, order_number_text, self.WAIT_TIME_MEDIUM)
            order_number = int(self.get_element_text(self.order_no, self.WAIT_TIME_MEDIUM).strip())

        return order_number
