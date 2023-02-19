from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Найти кнопку "Регистрация" и нажать её
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Найти кнопку "Войти в аккаунт" и нажать её
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

# Ввести логин и пароль
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Закрыть браузер
driver.quit()