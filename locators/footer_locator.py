import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FooterLocator:
    def getFacebookIcon(self):
        return self.driver.find_element(By.XPATH, '//*[@id="footer-bottom"]/div/ul/li[1]/a')

    def getTwitterIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[2]/a')

    def getGoogleIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[3]/a')

    def getLinkedInIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[4]/a')
    
    def getRssIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="footer-bottom"]/div/ul/li[5]/a')

    def getCopyRight(self):
        return self.driver.find_element(By.ID,'footer-info')