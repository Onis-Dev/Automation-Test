import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from common.environment import CONSTANTS

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1400,600")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.binary_location = "/usr/bin/google-chrome-stable"
chrome_options.add_argument('--ignore-certificate-errors')

def pytest_addoption(parser):
    parser.addoption("--url", action="store")

@pytest.fixture(scope="class")
def setup(request):
    web_driver = webdriver.Chrome(options=chrome_options, executable_path=CONSTANTS['driverConfig'].get('PATH'))
    url_value = request.config.option.url
    web_driver.get(url_value)
    request.cls.driver = web_driver
    
    yield web_driver
    web_driver.close()

# REDIRECT TO HOME PAGE
@pytest.fixture(scope="session")
def get_base_url(request):
    base_url = request.config.option.url
    base_url = base_url if base_url[-1] == "/" else base_url + '/'
    return base_url

# REDIRECT TO TRAINING PAGE
@pytest.fixture(scope="session")
def get_training_url(request):
    base_url = request.config.option.url
    training_url = base_url + CONSTANTS['HEADER'].get('TRAINING_LINK')
    return training_url

# REDIRECT TO TRAINING FRAMEWORK PAGE
@pytest.fixture(scope="session")
def get_training_af_url(request):
    base_url = request.config.option.url
    training_url = base_url + CONSTANTS['HEADER'].get('SUBMENU_AGILEFRAMEWORK')
    return training_url
