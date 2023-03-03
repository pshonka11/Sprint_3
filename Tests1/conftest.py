import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
