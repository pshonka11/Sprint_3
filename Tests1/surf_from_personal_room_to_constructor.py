from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_surf_from_personal_room_by_constructor():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Ввести логин и пароль
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Нажать кнопку "Личный кабинет"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

# Нажать кнопку "Контструктор"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()

    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "// h1[contains(text(), 'Соберите бургер')]"))).text == 'Соберите бургер'