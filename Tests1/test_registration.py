from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PagesLocators


def test_registration(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Найти кнопку "Регистрация" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.REGISTER)).click()

# Заполнить поля с именем, почтой и паролем

    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.LOGIN)).send_keys('Alena')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_127@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123427')

    # Найди кнопку "Регистрации" и кликни по ней
    WebDriverWait(get_driver, 5).until(EC.element_to_be_clickable(PagesLocators.REGISTER_ONE)).click()
    WebDriverWait(get_driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))


# проверяем что регистрация прошла успешно - переход на страницу авторизации
    current_url = get_driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'

