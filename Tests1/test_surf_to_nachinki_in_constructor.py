from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_surf_nachinki(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Ввести логин и пароль
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alena_vezdeneva_6_111@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

# Нажать кнопку "Войти"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()


    WebDriverWait(get_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span"))).click()

    fillings = WebDriverWait(get_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[3]/a[1]/p"))).text
    assert fillings == 'Мясо бессмертных моллюсков Protostomia'
