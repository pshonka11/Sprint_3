from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Найти кнопку "Регистрация" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Заполнить поля с именем, почтой и паролем
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alena')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('alena_vezdeneva_6_114@yandex.ru')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123454')

# Найти и нажать кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

# проверяем что регистрация прошла успешно - переход на страницу авторизации
    current_url = driver.current_url
    assert 'login' in current_url

# Закрыть браузер
    driver.quit()
