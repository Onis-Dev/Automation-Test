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

    CONST = CONSTANTS['TOP_HEADER']
    TITLES = CONSTANTS['TITLES_PAGES']
    
    @allure.title("Test social media icons")
    @allure.description(" Test if social media icons are displayed")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.topHeader_social_media_icons
    def test_social_media_icons(self):
        facebookIcon = Utils.is_displayed(self,TopHeaderLocator.get_facebook_icon(self))
        twitterIcon = Utils.is_displayed(self,TopHeaderLocator.get_twitter_icon(self))
        googleIcon = Utils.is_displayed(self,TopHeaderLocator.get_google_icon(self))
        linkedinIcon = Utils.is_displayed(self,TopHeaderLocator.get_linkedIn_icon(self))
        rssIcon = Utils.is_displayed(self,TopHeaderLocator.get_rss_icon(self))

        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert googleIcon, 'google icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
        assert rssIcon, 'rss icon is not being displayed'
    
    @allure.title("Test 'Contact Us' link redirect")
    @allure.description("Test if contact us link is displayed and working")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.topHeader_contactUs_link
    def test_contactUs_text(self, get_base_url):
        contactUs = TopHeaderLocator.get_contact_us(self)
        assert Utils.is_displayed(self,contactUs), 'contact us link is not being displayed'
        contactUs_path = get_base_url +  self.CONST.get('CONTACTUS_LINK')
        path = Utils.click_link(self, contactUs,self.TITLES.get('CONTACTUS_REGISTER_TITLE'), contactUs_path)
        assert path == contactUs_path, 'CONTACT US link is not working'
