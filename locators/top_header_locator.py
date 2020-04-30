import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 

class TopHeaderLocator:
    def getFacebookIcon(self):
        return self.driver.find_element(By.XPATH, '//*[@id="et-secondary-menu"]/ul[1]/li[1]/a')
    
    def getTwitterIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[2]/a')

    def getGoogleIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[3]/a')
    
    def getLinkedInIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[4]/a')

    def getRssIcon(self):
        return self.driver.find_element(By.XPATH,'//*[@id="et-secondary-menu"]/ul[1]/li[5]/a')

    def getContactUs(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#et-secondary-nav > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-4912 > a')
    
    def getPhone(self):
        return self.driver.find_element(By.ID,'et-info-phone')
    
    def getEmail(self):
        return self.driver.find_element(By.ID,'et-info-email')

