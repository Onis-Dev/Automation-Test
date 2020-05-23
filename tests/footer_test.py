import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.footer_locator import FooterLocator
from common.environment import CONSTANTS, PAGE_ELEMENTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
class TestFooter:

    ELEMENTS = PAGE_ELEMENTS['HOME']

    #FOOTER  HOME PAGE
    @allure.title("Test social media footer icons")
    @allure.description(" Test if social media footer icons are displayed")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.footer_social_media_icons
    def test_social_media_icons_footer(self):
        facebookIcon = Utils.is_displayed(self,FooterLocator.getFacebookIcon(self))
        twitterIcon = Utils.is_displayed(self,FooterLocator.getTwitterIcon(self))
        linkedinIcon = Utils.is_displayed(self,FooterLocator.getLinkedInIcon(self))
           
        assert facebookIcon, 'facebook icon is not being displayed'
        assert twitterIcon, 'twitter icon is not being displayed'
        assert linkedinIcon, 'linkedin icon is not being displayed'
  
    @allure.title("Test copyright footer ")
    @allure.description(" Test if copyright is displayed")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.footer_copyright
    def test_copyright_text(self):
        copyRight = Utils.is_displayed(self,FooterLocator.getCopyRight(self))
        assert copyRight, 'copyright  is not being displayed'
        

    