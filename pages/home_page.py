
from webium import Find, Finds
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#Pages
import pages
from pages.main_page import MainPage

class HomePage(MainPage):
    topSectionImage = Find(by= By.XPATH, value='//*[@id="post-39"]/div/div[1]/div/div[1]/div/img')
