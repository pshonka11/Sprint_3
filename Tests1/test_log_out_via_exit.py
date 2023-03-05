from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PagesLocators


def test_log_out_via_personal_room(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Личный кабинет" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PERSONAL_ACCOUNT)).click()

# Ввести логин и пароль
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_126@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123426')

# Нажать кнопку "Войти"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Найти кнопку "Личный кабинет" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PERSONAL_ACCOUNT)).click()

# Найти и нажать кнопку "Выход"

    WebDriverWait(get_driver, 5).until(EC.element_to_be_clickable(PagesLocators.EXIT_ONE)).click()

# Убедиться, что мы вышли из аккаунта и находимся на странице входа в аккаунт
    WebDriverWait(get_driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    current_url = get_driver.current_url

    assert current_url == 'https://stellarburgers.nomoreparties.site/login'