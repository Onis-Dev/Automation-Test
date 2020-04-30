import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains

class HeaderLocator:
    def getLogo(self):
        return self.driver.find_element(By.ID,'logo')
    
    def getHomeLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5121')

    def getTrainingLink(self):
        return self.driver.find_element(By.ID, 'menu-item-7212')

    def getSubmenuTraining(self):
        return (self.driver.find_element(By.ID, 'menu-item-5151'),
               self.driver.find_element(By.ID, 'menu-item-8080'),
               self.driver.find_element(By.ID, 'menu-item-5152'))
    
    def getServicesLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5598')

    def getEventslink(self):
        return self.driver.find_element(By.ID, 'menu-item-5174')
    
    def getAboutLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5580')
    
    def getSubmenuAbout(self):
        return (self.driver.find_element(By.ID, 'menu-item-5168'),
               self.driver.find_element(By.ID, 'menu-item-5169'),
               self.driver.find_element(By.ID, 'menu-item-4706'),
               self.driver.find_element(By.ID, 'menu-item-7943'))
        
    def getResourcesLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5581')
    
    def getSubmenuResources(self):
        return (self.driver.find_element(By.ID, 'menu-item-7771'),
               self.driver.find_element(By.ID, 'menu-item-5171'),
               self.driver.find_element(By.ID, 'menu-item-5176'),
               self.driver.find_element(By.ID, 'menu-item-5172'))

    def getBlogLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5173')

    def clickLink(self, element, page):
        element.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(page), message=f"Page timeout or is not loading {page}")
        return self.driver.current_url
    
    def hover_on_link(self,main_element):
        actions =chains(self.driver)
        actions.move_to_element(main_element).perform()



    