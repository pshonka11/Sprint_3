from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_log_in_via_forgot_password(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Найти кнопку "Забыли пароль" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()

# Найти кнопку "Войти в аккаунт" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

# Ввести логин и пароль
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    assert WebDriverWait(get_driver, 3).until(
    EC.visibility_of_element_located(
        (By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'
