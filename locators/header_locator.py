import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

class HeaderLocator:
    def getLogo(self):
        return Utils.find_element_by_id(self,'logo')
    
    def getHomeLink(self):
        return Utils.find_element_by_id(self, 'menu-item-5121')

    def getTrainingLink(self):
        return Utils.find_element_by_id(self, 'menu-item-7212')

    def getSubmenuTraining(self):
        return (Utils.find_element_by_id(self, 'menu-item-5151'),
               Utils.find_element_by_id(self, 'menu-item-8080'),
               Utils.find_element_by_id(self, 'menu-item-5152'))
    
    def getServicesLink(self):
        return Utils.find_element_by_id(self, 'menu-item-5598')

    def getEventslink(self):
        return Utils.find_element_by_id(self, 'menu-item-5174')
    
    def getAboutLink(self):
        return Utils.find_element_by_id(self, 'menu-item-5580')
    
    def getSubmenuAbout(self):
        return (Utils.find_element_by_id(self, 'menu-item-5168'),
               Utils.find_element_by_id(self, 'menu-item-5169'),
               Utils.find_element_by_id(self, 'menu-item-4706'),
               Utils.find_element_by_id(self, 'menu-item-7943'))
        
    def getResourcesLink(self):
        return Utils.find_element_by_id(self, 'menu-item-5581')
    
    def getSubmenuResources(self):
        return (Utils.find_element_by_id(self, 'menu-item-7771'),
               Utils.find_element_by_id(self, 'menu-item-5171'),
               Utils.find_element_by_id(self, 'menu-item-5176'),
               Utils.find_element_by_id(self, 'menu-item-5172'))

    def getBlogLink(self):
        return Utils.find_element_by_id(self, 'menu-item-5173')



    