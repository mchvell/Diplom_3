from selenium.webdriver.common.by import By


class MainPageLocators:
    TABS = {
        "bread": (By.XPATH, "//span[text()='Булки']"),
        "sauce": (By.XPATH, "//span[text()='Соусы']"),
        "topping": (By.XPATH, "//span[text()='Начинки']")
    }

    TABS_HEADERS = {
        "bread": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Булки']"),
        "sauce": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Соусы']"),
        "topping": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Начинки']")
    }

    SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")

    MODAL_WINDOW_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened') and contains(@class, 'Modal_modal')]")
    MODAL_WINDOW_HIDDEN = (By.XPATH, "//section[contains(@class, 'Modal_modal') and contains(@class, 'Modal_modal')][1]")
    MODAl_WINDOW_CLOSE = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    MODAL_WINDOW_ORDER_ACCESS = (By.XPATH, "//img[contains(@class, 'Modal_modal__image')]")


    ORDER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    SAUCE_COUNTER = (By.XPATH, "//p[normalize-space()='1']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    BREAD = {
        "fluorescent": (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"),
        "crater_bread": (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    }

    SAUCES = {
        "spice_x": (By.XPATH, "//img[@alt='Соус Spicy-X']"),
        "space_sauce": (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")
    }

    FILLINGS = {
        "protostomia": (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']"),
        "beef_meteo": (By.XPATH, "//img[@alt='Говяжий метеорит (отбивная)']")
    }


