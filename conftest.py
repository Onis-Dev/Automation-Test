import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1400,600")

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    web_driver = webdriver.Chrome(executable_path=r'/var/lib/jenkins/workspace/Automation/chromedriver')
    web_driver.get("https://smoothapps.com/")
    request.cls.driver = web_driver

    yield web_driver
    web_driver.close()