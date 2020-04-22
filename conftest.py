import pytest
import webium.driver
import webium.settings
import allure

from pages.home_page import HomePage

@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('w3c', False)
    return chrome_options

@pytest.fixture
def driver(driver,request,base_url):
    webium.driver._driver_instance = driver
    webium.settings.implicit_timeout = 10
    driver.implicitly_wait(webium.settings.implicit_timeout)
    driver.maximize_window()
    yield driver

@pytest.fixture
def home_page(driver, base_url):
    home_page = HomePage(driver=driver, url=base_url)
    home_page.open()
    return home_page