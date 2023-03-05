from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PagesLocators


def test_registration_failed_shows_error(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

    # Найти кнопку "Регистрация" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.REGISTER)).click()

    #Найти и заполнить данные для регистрации
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.LOGIN)).send_keys('Alena')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_128@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123')

    # Найди кнопку "Регистрации" и кликни по ней
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.REGISTER_ONE)).click()

    # явное ожидание для загрузки ошибки
    WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located((PagesLocators.TEXT_ERROR)))
    error_text = get_driver.find_element(*PagesLocators.TEXT_ERROR).text

    assert error_text == 'Некорректный пароль'