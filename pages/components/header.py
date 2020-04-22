from webium import Find
from selenium.webdriver.common.by import By

class Header(object): 
    navbar = Find(by=By.CSS_SELECTOR, value='#main-header')
    navbar_logo = Find(by=By.CSS_SELECTOR, value='#logo')
