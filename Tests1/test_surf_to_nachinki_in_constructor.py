from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PagesLocators


def test_surf_nachinki(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Ввести логин и пароль
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_126@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123426')

# Нажать кнопку "Войти"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Нажать кнопку "Начинки"
    WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located((PagesLocators.NACHINKI))).click()

# Убедиться, что мы находимся во вкладке 'Начинки'
    assert WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located((PagesLocators.CURRENT_TAB))).text == 'Начинки'
