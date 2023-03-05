from selenium.webdriver.common.by import By


class PagesLocators:
    ENTER = (By.CSS_SELECTOR, '[class^="button"]')
    REGISTER = (By.XPATH, '//*[@href="/register"]')
    LOGIN = (By.XPATH, '//input[contains(@class,"text") and preceding-sibling::label[contains(text(),"Имя")]]')
    EMAIL = (By.XPATH, '//input[contains(@class,"text") and preceding-sibling::label[contains(text(),"Email")]]')
    PASSWORD = (By.CSS_SELECTOR, '[type="password"]')
    REGISTER_ONE = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
    TEXT_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]")
    ORDER = (By.XPATH, '.// button[contains(text(), "Оформить заказ")]')
    PERSONAL_ACCOUNT = (By.XPATH, '//header//nav//a[contains(@href, "/account")]')
    FORGOT_PASS =(By.XPATH, '//div[starts-with(@class, "Auth_login")]//a[contains(@href, "/forgot-password")]')
    ENTER_ONE = (By.XPATH, '//div[starts-with(@class, "Auth_login")]//a[contains(@href, "/login")]')
    EXIT = (By.XPATH, '// button[contains(text(), "Выход")]')
    EXIT_ONE = (By.XPATH, '//button[contains(@class, "Account_button")]')
    ENTER_TWO = (By.XPATH, '//button[contains(text(),"Войти")]')
    STELLAR_BURGER = (By.XPATH, '//header//nav//div[contains(@class, "AppHeader_header__logo")]//a')
    CONSTRUCT_BURGER = (By.XPATH, '// h1[contains(text(), "Соберите бургер")]')
    CONSTRUCTOR = (By.XPATH, '//header//nav//ul/li/a[@href="/"]')
    BULKI = (By.XPATH, '//div[contains(@class, "tab_tab") and span[contains(text(), "Булки")]]')
    NACHINKI = (By.XPATH, '//div[contains(@class, "tab_tab") and span[contains(text(), "Начинки")]]')
    SOUSY = (By.XPATH, '//div[contains(@class, "tab_tab") and span[contains(text(), "Соусы")]]')
    CURRENT_TAB = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]//span')



print(type(PagesLocators.ENTER))