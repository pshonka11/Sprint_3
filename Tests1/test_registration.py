from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PagesLocators


def test_registration(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    #get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
    #get_driver.find_element(By.XPATH, "//*[contains(@class,'button')]").click()
    WebDriverWait(get_driver, 10).until(EC.element_to_be_clickable(PagesLocators.ENTER)).click()

# Найти кнопку "Регистрация" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Заполнить поля с именем, почтой и паролем
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alena')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('alena_vezdeneva_6_114@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123454')

# Найти и нажать кнопку "Зарегистрироваться"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

# проверяем что регистрация прошла успешно - переход на страницу авторизации
    current_url = get_driver.current_url
    assert 'login' in current_url

