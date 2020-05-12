import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_locator import HomeLocator
from common.environment import CONSTANTS
from common.utils import Utils


@pytest.mark.usefixtures("setup")
class TestAgileEvents:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']

    @allure.title("Test AGILE EVENTS LINK redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_view_all_upcoming_trainings_btn2
    def test_home_view_all_upcoming_trainings_btn2(self, get_base_url):
        view_all_upcoming_trainings_btn2 = HomeLocator.get_view_all_upcoming_trainings_btn2(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn2), 'AGILE EVENTS LINK is not being displayed'
       
       
    @allure.title("Test RESQUEST A SPEAKER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_uncoming_t_btn
    def test_home_request_uncoming_t_btn(self, get_base_url):
        request_uncoming_t_btn = HomeLocator.get_request_uncoming_t_btn(self)  
        assert Utils.is_displayed(self,request_uncoming_t_btn), 'RESQUEST A SPEAKER BUTTON is not being displayed'
       
       
    @allure.title("Test VIEW ALL UPCOMING EVENTS BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_view_all_upcoming_trainings_btn3
    def test_home_view_all_upcoming_trainings_btn3(self, get_base_url):
        view_all_upcoming_trainings_btn3 = HomeLocator.get_view_all_upcoming_trainings_btn3(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn3), 'AGILE EVENTS LINK is not being displayed'
       

    # @allure.title("Test AGILE DEVOPS MEETUP LINK redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_agile_devops_meetup_link
    # def test_home_agile_devops_meetup_link(self, get_base_url):
    #     agile_devops_meetup_link = HomeLocator.get_agile_devops_meetup_link(self)
    #     agile_devops_meetup_link_url = self.CONST.get('AGILE_DEVOPS_MEETUP_LINK')
    #     agile_devops_meetup_title = self.TITLES.get('AGILE_DEVOPS_MEETUP_TITLE')
    #     assert Utils.is_displayed(self,agile_devops_meetup_link), 'AGILE DEVOPS MEETUP LINK is not being displayed'
    #     path = Utils.click_link(self,agile_devops_meetup_link, agile_devops_meetup_title, agile_devops_meetup_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == agile_devops_meetup_link_url, 'AGILE DEVOPS MEETUP Link is not working'
        
        
    # @allure.title("Test AGILE DEVOPS MEETUP REGISTER BUTTON redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_agile_devops_meetup_register_btn
    # def test_home_agile_devops_meetup_register_btn(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     agile_devops_meetup_register_btn = HomeLocator.get_agile_devops_meetup_register_btn(self)
    #     agile_devops_meetup_register_btn_url = self.CONST.get('AGILE_DEVOPS_MEETUP_REGISTER_BTN')
    #     agile_devops_meetup_register_title = self.TITLES.get('AGILE_DEVOPS_MEETUP_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,agile_devops_meetup_register_btn), 'AGILE DEVOPS MEETUP REGISTER BUTTON is not being displayed'
    #     path = Utils.click_link(self,agile_devops_meetup_register_btn, agile_devops_meetup_register_title, agile_devops_meetup_register_btn_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == agile_devops_meetup_register_btn_url, 'AGILE DEVOPS MEETUP REGISTER Link is not working'

    # @allure.title("Test SCRUM PULSE WEBINAR LINK redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_scrum_pulse_webinar_link
    # def test_home_scrum_pulse_webinar_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     scrum_pulse_webinar_link = HomeLocator.get_scrum_pulse_webinar_link(self)
    #     scrum_pulse_webinar_link_url = self.CONST.get('SCRUM_PULSE_WEBINAR_LINK')
    #     scrum_pulse_webinar_title = self.TITLES.get('SCRUM_PULSE_WEBINAR_TITLE')
    #     assert Utils.is_displayed(self,scrum_pulse_webinar_link), 'SCRUM PULSE WEBINAR LINK is not being displayed'
    #     path = Utils.click_link(self,scrum_pulse_webinar_link, scrum_pulse_webinar_title, scrum_pulse_webinar_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == scrum_pulse_webinar_link_url, 'SCRUM PULSE WEBINAR Link is not working'
        
        
    @allure.title("Test SCRUM PULSE WEBINAR REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_scrum_pulse_webinar_btn
    def test_home_scrum_pulse_webinar_link2(self, get_base_url):
        self.driver.get(get_base_url)
        scrum_pulse_webinar_link2 = HomeLocator.get_scrum_pulse_webinar_link2(self)
        assert Utils.is_displayed(self,scrum_pulse_webinar_link2), 'SCRUM PULSE WEBINAR REGISTER BUTTON is not being displayed'