import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

class FooterLocator:
    """Get facebook icon element"""
    def getFacebookIcon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('FACEBOOK_ICON_FOOTER_XPATH'))
    
    """Get twitter icon element"""
    def getTwitterIcon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('TWITTER_ICON_FOOTER_XPATH'))

    """Get linkedIn icon element"""
    def getLinkedInIcon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('LINKEDIN_ICON_FOOTER_XPATH'))

    """Get CopyRight element"""   
    def getCopyRight(self):
        return Utils.find_element_by_id(self, self.ELEMENTS.get('COPYRIGHT_ID'))