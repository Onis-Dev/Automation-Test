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


@pytest.fixture(scope="session")
def get_base_url(request):
    base_url = request.config.option.url
    base_url = base_url if base_url[-1] == "/" else base_url + '/'
    return base_url

