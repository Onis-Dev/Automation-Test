import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.utils import Utils

class FooterLocator:
    def getFacebookIcon(self):
        return Utils.find_element_by_xpath(self, '//*[@id="footer-bottom"]/div/ul/li[1]/a')

    def getTwitterIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="footer-bottom"]/div/ul/li[2]/a')

    def getGoogleIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="footer-bottom"]/div/ul/li[3]/a')

    def getLinkedInIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="footer-bottom"]/div/ul/li[4]/a')
    
    def getRssIcon(self):
        return Utils.find_element_by_xpath(self,'//*[@id="footer-bottom"]/div/ul/li[5]/a')

    def getCopyRight(self):
        return Utils.find_element_by_id(self,'footer-info')