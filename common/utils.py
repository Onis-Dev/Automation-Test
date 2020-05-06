import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains

""" This class contains all shared methods that can be used in all tests """
class Utils:

    """ 
        Function that performs click event in the received element.
        Waits the specific page to be loaded (with a timeout of 10 seconds) 
        then returns the actual URL.
        (this function is used in elements that need to redirect).
    """
    def click_link(self, element, page):
        element.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(page),  message="Page is not loading or it produced a timeout trying to redirect {}".format(page))
        return self.driver.current_url
    
    """ Function that performs a hover effect on a specific element. """
    def hover_on_link(self,main_element):
        actions =chains(self.driver)
        actions.move_to_element(main_element).perform()
    
    """ Finds an element by id and handles exception in case it doesn't exist"""
    def find_element_by_id(self, locator):
        try:
            return self.driver.find_element(By.ID, locator)
        except:
            return None

    """ Finds an element by xpath and handles exception in case it doesn't exist"""
    def find_element_by_xpath(self, locator):
        try:
            return self.driver.find_element(By.XPATH, locator)
        except:
            return None
    
    """ Finds an element by css selector and handles exception in case it doesn't exist"""
    def find_element_by_css_selector(self, locator):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        except:
            return None
    
    """ verify if an element is displayed in the screen"""
    def is_displayed(self, element):
        return element.is_displayed() if element != None else False
