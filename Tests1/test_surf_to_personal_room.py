# У меня этот тест не валится
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_surf_personal_room(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Ввести логин и пароль
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Нажать кнопку "Личный кабинет"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()

    WebDriverWait(get_driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "// button[contains(text(), 'Выход')]"))).click()
    assert WebDriverWait(get_driver, 3).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Войти')]"))).text == 'Войти'

