import pytest
import allure
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.header_locator import HeaderLocator
from common.environment import CONSTANTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
@allure.title("All Training tests")
class TestTraining:
    pass
    # @pytest.mark.training_title
    # def test_training_title(self):
    #     title = self.driver.find_element(By.XPATH,'//*[@id="post-1899"]/div/div[1]/div/div/div/h1') 
    #     assert title.text == 'Agile Training'
