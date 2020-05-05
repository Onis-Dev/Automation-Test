import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.utils import Utils

class TopHeaderLocator:
    def getFacebookIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[1]/a')
    
    def getTwitterIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[2]/a')

    def getGoogleIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[3]/a')
    
    def getLinkedInIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[4]/a')

    def getRssIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="et-secondary-menu"]/ul[1]/li[5]/a')

    def getContactUs(self):
        return Utils.find_element_by_css_selector(self, '#et-secondary-nav > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-4912 > a')
    
    def getPhone(self):
        return Utils.find_element_by_id(self,'et-info-phone')
    
    def getEmail(self):
        return Utils.find_element_by_id(self,'et-info-email')

