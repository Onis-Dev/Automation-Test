import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains

class Utils:
    def clickLink(self, element, page):
        element.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(page),  message="Page is not loading or it produced a timeout trying to redirect {}".format(page))
        return self.driver.current_url
    
    def hover_on_link(self,main_element):
        actions =chains(self.driver)
        actions.move_to_element(main_element).perform()
    
    def find_element_by_id(self, locator):
        try:
            return self.driver.find_element(By.ID, locator)
        except:
            return None
    def find_element_by_xpath(self, locator):
        try:
            return self.driver.find_element(By.XPATH, locator)
        except:
            return None
    
    def find_element_by_css_selector(self, locator):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        except:
            return None
    
    def is_displayed(self, element):
        return element.is_displayed() if element != None else False
