import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.utils import Utils

"""Class to get all elements from Top Header section"""
class TopHeaderLocator:

    """Get facebook icon element"""
    def get_facebook_icon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('FACEBOOK_ICON_XPATH'))
    
    """Get twitter icon element"""
    def get_twitter_icon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('TWITTER_ICON_XPATH'))

    """Get google icon element"""
    def get_google_icon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('GOOGLE_ICON_XPATH'))
    
    """Get linkedIn icon element"""
    def get_linkedIn_icon(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('LINKEDIN_ICON_XPATH'))
                                               
    """Get rss icon element"""
    def get_rss_icon(self):
       return Utils.find_element_by_xpath(self, self.ELEMENTS.get('RSS_ICON_XPATH'))

    """Get Contact link element"""
    def get_contact_us(self):
        return Utils.find_element_by_css_selector(self, self.ELEMENTS.get('CONTACT_US_CSS'))

