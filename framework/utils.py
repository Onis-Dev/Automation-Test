import webium
from webium.driver import get_driver
from webium.settings import implicit_timeout
from webium.base_page import is_element_present as base_is_element_present
from selenium.webdriver.support.expected_conditions import invisibility_of_element_located, number_of_windows_to_be
from selenium.webdriver.support.wait import WebDriverWait

def wait_until(predicate, message='', timeout=implicit_timeout):
    return WebDriverWait(get_driver(), timeout).until(predicate, message)


def wait_until_invisibility_of_element_located(locator, message='', timeout=implicit_timeout):
    driver = get_driver()
    try:
        driver.implicitly_wait(0)
        return WebDriverWait(get_driver(), timeout).until(invisibility_of_element_located(locator), message)
    finally:
        driver.implicitly_wait(webium.settings.implicit_timeout)

def is_element_present(self, element_name, just_in_dom=False, timeout=0):
    return base_is_element_present(self, element_name, just_in_dom, timeout)