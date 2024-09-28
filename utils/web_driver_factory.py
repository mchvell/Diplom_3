from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_type):
        if browser_type == "chrome":
            return webdriver.Chrome()
        elif browser_type == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Не поддерживаемый браузер: {browser_type}")
