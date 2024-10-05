import allure
import pytest
from pages.auth_page import AuthPageHelper
from pages.main_page import MainPageHelper
from utils.web_driver_factory import WebDriverFactory
from api_modules.api_modules import UserAPI  # Импортируем UserAPI для работы с API


@allure.step("Создание пользователя на уровне теста")
@pytest.fixture(scope="function")
def user_create():
    user_api = UserAPI()  # Создаем экземпляр UserAPI
    user_credentials, jwt = user_api.create_user()  # Создаем пользователя
    yield user_credentials, jwt  # Возвращаем и учетные данные, и JWT
    user_api.delete_user(jwt)  # Удаляем пользователя после теста


@allure.step("Создаем экземпляр браузера исходя из параметров теста")
@pytest.fixture(scope="function")
def browser(request):
    # Получаем тип браузера через параметр теста
    browser_type = request.param
    driver = WebDriverFactory.get_driver(browser_type=browser_type)
    yield driver
    driver.quit()


@allure.step("Авторизация пользователя")
@pytest.fixture(scope="function")
def authorization(browser, user_create):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site()

    email = user_create[0]["email"]
    password = user_create[0]["password"]

    auth_page.fill_auth_form(email=email, password=password)
    auth_page.click_enter_button()

    yield user_create[1]  # Возвращаем JWT


@allure.step("Создание бургера")
@pytest.fixture(scope="function")
def create_burger(browser, authorization):
    main_page = MainPageHelper(browser)

    main_page.drag_and_drop_item(type="sauce", name="spice_x")
    main_page.drag_and_drop_item(type="bread", name="fluorescent")

    main_page.set_tab("topping")
    main_page.drag_and_drop_item(type="filling", name="protostomia")

    main_page.click_on_order_button()
    order_no = main_page.get_order_number()
    main_page.close_modal_window()

    return order_no
