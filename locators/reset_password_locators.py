from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    ENTER_CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input')]/*[name()='svg']")
    PASSWORD_FIELD_HIDDEN = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_type_password')]")
    PASSWORD_FIELD_SHOWN = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_status_active')]")