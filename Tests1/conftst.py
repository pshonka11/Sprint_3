import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url='https://stellarburgers.nomoreparties.site'
@pytest.fixture
def driver():
    browser_driver = webdriver.Chrome()
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()

@pytest.fixture
def driver_signin():
    browser_driver = webdriver.Chrome()
    browser_driver.get(url)
    browser_driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    browser_driver.find_element(By.XPATH, "//fieldset[1]/div[1]/div[1]/input[1]").send_keys("alena_vezdeneva_6_111@yandex.ru")
    browser_driver.find_element(By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20']//input[@type='password']").send_keys("123456")
    browser_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    WebDriverWait(browser_driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

    yield browser_driver
    browser_driver.quit()