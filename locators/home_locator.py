import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

class HomeLocator:

    def getLearnMoreBtn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[1]/div/div[2]/div[2]/a')