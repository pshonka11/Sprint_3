from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.page_locators import PagesLocators


def test_surf_from_personal_room_by_constructor(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Ввести логин и пароль
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_126@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123426')

# Нажать кнопку "Войти"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Нажать кнопку "Личный кабинет"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PERSONAL_ACCOUNT)).click()

# Нажать кнопку "Контструктор"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.CONSTRUCTOR)).click()

# Убедиться, что мы находимся в конструкторе и можем собирать бургер
    assert WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located((PagesLocators.CONSTRUCT_BURGER))).text == 'Соберите бургер'