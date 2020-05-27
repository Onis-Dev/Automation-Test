import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from locators.home_locator import HomeLocator
from common.environment import CONSTANTS, PAGE_ELEMENTS
from common.utils import Utils


@pytest.mark.usefixtures("setup")
class TestEvents:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']
    CONSTHEADER = CONSTANTS['HEADER']
    ELEMENTS = PAGE_ELEMENTS['HOME']

    #AGILE EVENTS
    @allure.title("Test AGILE EVENTS LINK is displayed") 
    @allure.description(" Test if link is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_view_all_upcoming_trainings_btn2
    def test_home_view_all_upcoming_trainings_btn2(self, get_base_url):
        view_all_upcoming_trainings_btn2 = HomeLocator.get_view_all_upcoming_trainings_btn2(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn2), 'AGILE EVENTS LINK is not being displayed'
       
       
    @allure.title("Test RESQUEST A SPEAKER BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_uncoming_t_btn
    def test_home_request_uncoming_t_btn(self, get_base_url):
        request_uncoming_t_btn = HomeLocator.get_request_uncoming_t_btn(self)  
        assert Utils.is_displayed(self,request_uncoming_t_btn), 'RESQUEST A SPEAKER BUTTON is not being displayed'
       
       
    @allure.title("Test VIEW ALL UPCOMING EVENTS BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_view_all_upcoming_trainings_btn3
    def test_home_view_all_upcoming_trainings_btn3(self, get_base_url):
        view_all_upcoming_trainings_btn3 = HomeLocator.get_view_all_upcoming_trainings_btn3(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn3), 'AGILE EVENTS LINK is not being displayed'           


    @allure.title("Test AGILE BLOG SLIDER  button is displayed and working") 
    @allure.description(" Test if AGILE BLOG slider is working correctly")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_blog_slider
    def test_home_agile_blog_slider(self, get_base_url):
        slider = HomeLocator.get_agile_blog_slider(self)
        assert Utils.is_displayed(self, slider), "slider content is not being displayed"
        slider_first_control = HomeLocator.get_agile_blog_controllers(self)[0]
        slider_first_control.click()
        sleep(1)
        slider_second_control = HomeLocator.get_agile_blog_controllers(self)[1]
        slider_second_control.click()
        slider_first_control = HomeLocator.get_agile_blog_controllers(self)[0]
        is_active_on_change= slider_first_control.get_attribute('class')
        assert  "active" not in is_active_on_change, "AGILE BLOG SLIDER is not working correctly"