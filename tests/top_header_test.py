import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.top_header_locator import TopHeaderLocator
from common.environment import CONSTANTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
class TestTopHeader:

    CONST = CONSTANTS['topHeader']

    @allure.title("Test social media icons")
    @allure.description(" Test if social media icons are displayed")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.topHeader_social_media_icons
    def test_social_media_icons(self):
        facebookIcon = Utils.is_displayed(self,TopHeaderLocator.getFacebookIcon(self))
        twitterIcon = Utils.is_displayed(self,TopHeaderLocator.getTwitterIcon(self))
        googleIcon = Utils.is_displayed(self,TopHeaderLocator.getGoogleIcon(self))
        linkedinIcon = Utils.is_displayed(self,TopHeaderLocator.getLinkedInIcon(self))
        rssIcon = Utils.is_displayed(self,TopHeaderLocator.getRssIcon(self))

        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'
    
    @allure.title("Test 'Contact Us' link redirect")
    @allure.description("Test if contact us link is displayed and working")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.topHeader_contactUs_link
    def test_contactUs_text(self):
        contactUs = Utils.is_displayed(self,TopHeaderLocator.getContactUs(self))
        assert contactUs, 'contact us link is not being displayed'
        path = Utils.clickLink(self,contactUs,self.CONST.get('CONTACTUS_LINK'))
        assert path == self.CONST.get('CONTACTUS_LINK'), 'CONTACT US link is not working'
