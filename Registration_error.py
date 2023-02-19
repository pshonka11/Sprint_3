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

# Заполнить поля с именем, почтой и паролем
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alena')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('alena_vezdeneva_6_123@yandex.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123')

# Найти и нажать кнопку "Зарегистрироваться"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Найди надпись об ошибке, получить её текст и проверить, что он равен 'Некорректный пароль'
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'

# Закрыть браузер
driver.quit()