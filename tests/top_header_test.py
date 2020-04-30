import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.top_header_locator import TopHeaderLocator
from common.environment import CONSTANTS

@pytest.mark.usefixtures("setup")
class TestTopHeader:

    CONST = CONSTANTS['topHeader']

    def test_social_media_icons(self):
        facebookIcon = TopHeaderLocator.getFacebookIcon(self).is_displayed()
        twitterIcon = TopHeaderLocator.getTwitterIcon(self).is_displayed()
        googleIcon = TopHeaderLocator.getGoogleIcon(self).is_displayed()
        linkedinIcon = TopHeaderLocator.getLinkedInIcon(self).is_displayed()
        rssIcon = TopHeaderLocator.getRssIcon(self).is_displayed()

        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'
    
    def test_contactUs_text(self):
        contactUs = TopHeaderLocator.getContactUs(self).text
        assert contactUs == self.CONST.get('CONTACTUS'), 'contact us link is not being displayed'
    
    def test_phone_email_text(self):
        phone = TopHeaderLocator.getPhone(self).text
        email = TopHeaderLocator.getEmail(self).text
        assert phone == self.CONST.get('PHONE'), 'phone is not being displayed or it is wrong'
        assert email == self.CONST.get('EMAIL'), 'email is not being displayed or it is wrong'
