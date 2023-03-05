from locators.page_locators import PagesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_surf_personal_room(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Ввести логин и пароль
    # Ввести логин и пароль
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_126@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123426')

# Нажать кнопку "Войти"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Нажать кнопку "Личный кабинет"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PERSONAL_ACCOUNT)).click()

# Найти и нажать кнопку "Выход"
    WebDriverWait(get_driver, 5).until(EC.element_to_be_clickable(PagesLocators.EXIT_ONE)).click()

# Убедиться, что мы находимся на странице входа в аккаунт, где есть кнопка "Войти"
    assert WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located((PagesLocators.ENTER_TWO))).text == 'Войти'
