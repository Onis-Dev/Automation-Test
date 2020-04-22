
from webium import BasePage, Find, Finds
from webium.driver import get_driver
from selenium.webdriver.support.expected_conditions import alert_is_present, visibility_of
from selenium.webdriver.common.by import By
from framework.utils import wait_until, wait_until_invisibility_of_element_located, is_element_present
from pages.components import Header

class MainPage(BasePage):
    header = Find(Header)
    page_content = Find(by=By.CSS_SELECTOR, value='#page-container')

    def is_opened(self):
        return self.is_element_present('page_content', timeout=20)

    def wait_page_is_opened(self):
        wait_until(visibility_of(self.page_content),message='Fail to open Page "{0}"'.format(self.__class__.__name__))
