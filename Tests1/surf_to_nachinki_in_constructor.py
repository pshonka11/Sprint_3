from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_surf_nachinki():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Ввести логин и пароль
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()


    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span"))).click()

    fillings = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[3]/a[1]/p"))).text
    assert fillings == 'Мясо бессмертных моллюсков Protostomia'

# Закрыть браузер
    driver.quit()