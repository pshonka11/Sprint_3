# У меня этот тест не валится
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_surf_to_bulki_in_constructor(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Ввести логин и пароль
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Нажать кнопку "Соусы"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()

# Нажать кнопку "Булки"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()

    WebDriverWait(get_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[2]/span"))).click()
    WebDriverWait(get_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[1]/span"))).click()

    rolls = WebDriverWait(get_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[1]/a[1]/p"))).text
    assert rolls == 'Флюоресцентная булка R2-D3'
