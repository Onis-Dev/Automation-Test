from webium import Find
from selenium.webdriver.common.by import By

class Footer(object):
    footerCopyright = Find(by=By.CSS_SELECTOR, value='#footer-info')