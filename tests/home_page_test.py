import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestHome:
    def test_logo_top_section(self):
        status = self.driver.find_element(By.ID,'logo').is_displayed()
        assert status, 'Logo is not present'
