from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_log_out_via_personal_room():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Личный кабинет" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

# Ввести логин и пароль
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Найти кнопку "Личный кабинет" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "// button[contains(text(), 'Выход')]"))).click()

    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Войти')]"))).text == 'Войти'

# Закрыть браузер
    driver.quit()