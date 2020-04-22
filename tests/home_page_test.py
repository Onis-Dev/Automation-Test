import pytest
import allure
from selenium.webdriver.common.by import By

from pages.home_page import HomePage

def test_verify_logo(home_page):
    assert home_page.is_element_present('topSectionImage'), 'Logo is not present'
