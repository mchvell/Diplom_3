import allure

from pages.base_page import BasePage
from locators.nav_bar_locators import NavBarLocators


class NavBarHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar_tabs = NavBarLocators.NAVBAR_TABS

    @allure.step("Переключить вкладку верхнего навбара")
    def switch_tab(self, nav_tab):
        nav_bar_locator = self.nav_bar_tabs.get(nav_tab)
        return self.find_element(nav_bar_locator, 15).click()
