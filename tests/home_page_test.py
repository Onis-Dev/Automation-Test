import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_locator import HomeLocator
from common.environment import CONSTANTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
class TestHome:

    CONST = CONSTANTS['HOME']

    def test_learn_more_redirect(self):
        learn_more_btn = HomeLocator.getLearnMoreBtn(self)
        assert Utils.is_displayed(self,learn_more_btn), 'Learn More button is being displayed'
        path = Utils.clickLink(self, learn_more_btn, self.CONST.get('LEARN_MORE_REDIRECT'))
        assert path == self.CONST.get('LEARN_MORE_REDIRECT'), 'LEARN MORE REDIRECT is not working'
