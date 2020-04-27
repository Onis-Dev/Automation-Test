import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.environment import CONSTANTS

@pytest.mark.usefixtures("setup")
class TestFooter:

    CONST = CONSTANTS['footer']

    def test_social_media_icons_footer(self):
        facebookIcon = self.driver.find_element(By.XPATH, '//*[@id="footer-bottom"]/div/ul/li[1]/a').is_displayed()
        twitterIcon = self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[2]/a').is_displayed()
        googleIcon = self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[3]/a').is_displayed()
        linkedinIcon = self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[4]/a').is_displayed()
        rssIcon = self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[5]/a').is_displayed()
       
        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'

    def test_copyright_text(self):
        copyRigth = self.driver.find_element(By.ID,'footer-info').text
        print (copyRigth, '********************')
        assert copyRigth == self.CONST.get('COPYRIGHT'), 'copyright  is not being displayed'
        

    