import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.environment import CONSTANTS

@pytest.mark.usefixtures("setup")
class TestTopHeader:

    CONST = CONSTANTS['topHeader']

    def test_social_media_icons(self):
        facebookIcon = self.driver.find_element(By.XPATH, '//*[@id="et-secondary-menu"]/ul[1]/li[1]/a').is_displayed()
        twitterIcon = self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[2]/a').is_displayed()
        googleIcon = self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[3]/a').is_displayed()
        linkedinIcon = self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[4]/a').is_displayed()
        rssIcon = self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[5]/a').is_displayed()

        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'
    
    def test_contactUs_text(self):
        contactUs = self.driver.find_element_by_css_selector('#et-secondary-nav > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-4912 > a').text
        assert contactUs == self.CONST.get('CONTACTUS'), 'contact us link is not being displayed'
    
    def test_phone_email_text(self):
        phone = self.driver.find_element(By.ID,'et-info-phone').text
        email = self.driver.find_element(By.ID,'et-info-email').text
        assert phone == self.CONST.get('PHONE'), 'phone is not being displayed or it is wrong'
        assert email == self.CONST.get('EMAIL'), 'email is not being displayed or it is wrong'
