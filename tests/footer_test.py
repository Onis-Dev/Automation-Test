import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.footer_locator import FooterLocator
from common.environment import CONSTANTS

@pytest.mark.usefixtures("setup")
class TestFooter:

    CONST = CONSTANTS['footer']

    def test_social_media_icons_footer(self):
        facebookIcon = FooterLocator.getFacebookIcon(self).is_displayed()
        twitterIcon = FooterLocator.getTwitterIcon(self).is_displayed()
        googleIcon = FooterLocator.getGoogleIcon(self).is_displayed()
        linkedinIcon = FooterLocator.getLinkedInIcon(self).is_displayed()
        rssIcon = FooterLocator.getRssIcon(self).is_displayed()
       
        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'

    def test_copyright_text(self):
        copyRigth = FooterLocator.getCopyRight(self).text
        assert copyRigth == self.CONST.get('COPYRIGHT'), 'copyright  is not being displayed'
        

    