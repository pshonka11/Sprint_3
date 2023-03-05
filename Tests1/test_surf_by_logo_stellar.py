from locators.page_locators import PagesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_transition_by_logo_stellar(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site/")

# Найти кнопку "Войти" и нажать её
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()


# Ввести логин и пароль
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.EMAIL)).send_keys('alena_vezdeneva_6_126@yandex.ru')
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.PASSWORD)).send_keys('123426')

# Нажать кнопку "Войти"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Нажать кнопку "Личный кабинет"
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

#Нажать кнопку stellar burger
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.STELLAR_BURGER)).click()
    assert WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located((PagesLocators.CONSTRUCT_BURGER))).text == 'Соберите бургер'
