import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.footer_locator import FooterLocator
from common.environment import CONSTANTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
class TestFooter:

    CONST = CONSTANTS['footer']

    def test_social_media_icons_footer(self):
        facebookIcon = Utils.is_displayed(self,FooterLocator.getFacebookIcon(self))
        twitterIcon = Utils.is_displayed(self,FooterLocator.getTwitterIcon(self))
        googleIcon = Utils.is_displayed(self,FooterLocator.getGoogleIcon(self))
        linkedinIcon = Utils.is_displayed(self,FooterLocator.getLinkedInIcon(self))
        rssIcon = Utils.is_displayed(self,FooterLocator.getRssIcon(self))
       
        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'

    def test_copyright_text(self):
        copyRigth = FooterLocator.getCopyRight(self)
        assert Utils.is_displayed(self, copyRigth)
        assert copyRigth.text == self.CONST.get('COPYRIGHT'), 'copyright  is not being displayed'
        

    