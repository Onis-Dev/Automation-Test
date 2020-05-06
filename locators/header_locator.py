import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

"""Class to get all elements from Header section"""
class HeaderLocator:

    """Get Home link element"""
    def get_home_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5121')

    """Get Training link element"""
    def get_training_link(self):
        return Utils.find_element_by_id(self, 'menu-item-7212')

    """Get Training submenu elements"""
    def get_submenu_training(self):
        return (Utils.find_element_by_id(self, 'menu-item-5151'),
               Utils.find_element_by_id(self, 'menu-item-8080'),
               Utils.find_element_by_id(self, 'menu-item-5152'))
    
    """Get Services link element"""
    def get_services_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5598')

    """Get Events link element"""
    def get_events_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5174')
    
    """Get About link element"""
    def get_about_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5580')
    
    """Get About Submenu elements"""
    def get_submenu_about(self):
        return (Utils.find_element_by_id(self, 'menu-item-5168'),
               Utils.find_element_by_id(self, 'menu-item-5169'),
               Utils.find_element_by_id(self, 'menu-item-4706'),
               Utils.find_element_by_id(self, 'menu-item-7943'))
    
    """Get Resources link element"""
    def get_resources_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5581')
    
    """Get Resources Submenu elements"""
    def get_submenu_resources(self):
        return (Utils.find_element_by_id(self, 'menu-item-7771'),
               Utils.find_element_by_id(self, 'menu-item-5171'),
               Utils.find_element_by_id(self, 'menu-item-5176'),
               Utils.find_element_by_id(self, 'menu-item-5172'))

    """Get Blog link element"""
    def get_blog_link(self):
        return Utils.find_element_by_id(self, 'menu-item-5173')



    