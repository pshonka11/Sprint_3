from selenium.webdriver.common.by import By


class PagesLocators:
    ENTER = (By.CSS_SELECTOR, '[class^="button"]')


print(type(PagesLocators.ENTER))