from selenium.webdriver.common.by import By


def test_registration_failed_shows_error(get_driver):
    get_driver.get("https://stellarburgers.nomoreparties.site")

# Найти кнопку "Войти" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

# Найти кнопку "Регистрация" и нажать её
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

# Заполнить поля с именем, почтой и паролем
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alena')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('alena_vezdeneva_6_123@yandex.ru')
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123')

# Найти и нажать кнопку "Зарегистрироваться"
    get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

# Найди надпись об ошибке, получить её текст и проверить, что он равен 'Некорректный пароль'
    assert get_driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'
