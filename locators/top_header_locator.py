import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.utils import Utils

class TopHeaderLocator:

    """Get facebook icon element"""
    def get_facebook_icon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[1]/a')
    
    """Get twitter icon element"""
    def get_twitter_icon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[2]/a')

    """Get google icon element"""
    def get_google_icon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[3]/a')
    
    """Get linkedIn icon element"""
    def get_linkedIn_icon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[4]/a')

    """Get rss icon element"""
    def get_rss_icon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[5]/a')

    """Get Contact link element"""
    def get_contact_us(self):
        return Utils.find_element_by_css_selector(self, '#et-secondary-nav > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-4912 > a')

