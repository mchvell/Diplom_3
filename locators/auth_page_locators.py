from selenium.webdriver.common.by import By


class AuthLocators:
    INPUTS = {
        "email": (By.XPATH, "//input[@name='name']"),
        "password": (By.XPATH, "//input[@type='password']")
    }

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

    LINKS = {
        "registration": (By.XPATH, "//a[text()='Зарегистрироваться']"),
        "reset_password": (By.XPATH, "//a[text()='Восстановить пароль']")
    }
