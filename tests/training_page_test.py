import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.environment import CONSTANTS, PAGE_ELEMENTS
from common.utils import Utils
from locators.training_locator import TrainingLocator
from locators.header_locator import HeaderLocator

@pytest.mark.usefixtures("setup")
class TestTraining:

    CONST = CONSTANTS['HOME']
    CONSTHEADER = CONSTANTS['HEADER']
    TITLES = CONSTANTS['TITLES_PAGES']
    ELEMENTS = PAGE_ELEMENTS['HOME']
    ELEMENTS = PAGE_ELEMENTS['TRAINING']

    @allure.title("Test TRAINING LINK redirect is working") 
    @allure.description(" Test if link redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_link
    def test_training_link(self, get_base_url):
        training_link = HeaderLocator.get_training_link(self)
        training_url = get_base_url + self.CONSTHEADER.get('TRAINING_LINK')
        path = Utils.click_link(self,training_link, self.TITLES.get('TRAINING_TITLE'),training_url) 
        assert path == training_url, 'TRAINING link is not working'


    @allure.title("Test REQUEST CUSTOM TRAINING BUTTON in training page, is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_request_custom_training_btn
    def test_training_request_custom_training_btn(self, get_base_url):
        t_request_custom_training_btn = TrainingLocator.get_t_request_custom_training_btn(self)
        t_request_custom_training_btn_url = get_base_url + self.CONST.get('CONTACTUS_REGISTER_BTN')
        contactus_register_title = self.TITLES.get('CONTACTUS_REGISTER_TITLE')
        assert Utils.is_displayed(self,t_request_custom_training_btn), 'REQUEST CUSTOM TRAINING BUTTON in training page is not being displayed'
        path = Utils.click_link(self,t_request_custom_training_btn, contactus_register_title, t_request_custom_training_btn_url) 
        assert path == t_request_custom_training_btn_url, 'REQUEST CUSTOM TRAINING LINK in training page is not working'

    

    @allure.title("Test VIEW ALL UPCOMING TRAININGS BUTTON in training page, is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_view_all_upcoming_trainings_btn
    def test_training_view_all_upcoming_trainings_btn(self, get_base_url, get_training_url):
        self.driver.get(get_training_url)
        t_view_all_upcoming_trainings_btn = TrainingLocator.get_t_view_all_upcoming_trainings_btn(self)
        t_view_all_upcoming_trainings_btn_url = get_base_url + self.CONST.get('VIEW_ALL_UPCOMING_TRAININGS_BTN')
        view_all_upcoming_trainings_title = self.TITLES.get('VIEW_ALL_UPCOMING_TRAININGS_TITLE')
        assert Utils.is_displayed(self,t_view_all_upcoming_trainings_btn), 'VIEW ALL UPCOMING TRAININGS BUTTON in training page is not being displayed'
        path = Utils.click_link(self,t_view_all_upcoming_trainings_btn, view_all_upcoming_trainings_title, t_view_all_upcoming_trainings_btn_url) 
        assert path == t_view_all_upcoming_trainings_btn_url, 'VIEW ALL UPCOMING TRAININGS LINK in training page is not working'


    #CUSTOM TRAINING
       
    @allure.title("Test CUSTOM TRAINING LINK in training page, is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_request_ct_btn
    def test_training_request_ct_btn(self, get_training_url):
        self.driver.get(get_training_url)
        t_request_ct_btn = TrainingLocator.get_t_request_ct_btn(self)  
        assert Utils.is_displayed(self,t_request_ct_btn), 'CUSTOM TRAINING LINK in training page is not being displayed'

    #AGILE FRAMEWORK PAGE

    @allure.title("Test AGILE FRAMEWORK LINK redirect is working") 
    @allure.description(" Test if link redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_agile_framework_link
    def test_training_agile_framework_link(self, get_base_url):
        self.driver.get(get_base_url)
        training_link = HeaderLocator.get_training_link(self)
       # assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_framework_link = HeaderLocator.get_submenu_training(self)[0]
        agile_framework_url = get_base_url + self.CONSTHEADER.get('SUBMENU_AGILEFRAMEWORK')
        path = Utils.click_link(self,agile_framework_link, self.TITLES.get('AGILE_FRAMEWORK_TITLE'),agile_framework_url) 
        assert path == agile_framework_url, 'TRAINING link is not working'

    @allure.title("Test REQUEST CUSTOM TRAINING BUTTON in AGILE FRAMEWORK page, is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_af_request_custom_training_btn
    def test_training_af_request_custom_training_btn(self, get_base_url):
        af_request_custom_training_btn = TrainingLocator.get_af_request_custom_training_btn(self)
        af_request_custom_training_btn_url = get_base_url + self.CONST.get('CONTACTUS_REGISTER_BTN')
        contactus_register_title = self.TITLES.get('CONTACTUS_REGISTER_TITLE')
        assert Utils.is_displayed(self,af_request_custom_training_btn), 'REQUEST CUSTOM TRAINING BUTTON in AGILE FRAMEWORK page is not being displayed'
        path = Utils.click_link(self,af_request_custom_training_btn, contactus_register_title, af_request_custom_training_btn_url) 
        assert path == af_request_custom_training_btn_url, 'REQUEST CUSTOM TRAINING LINK in AGILE FRAMEWORK page is not working'

    @allure.title("Test VIEW ALL UPCOMING TRAININGS BUTTON in Agile Framework page, is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_af_view_all_upcoming_trainings_btn
    def test_training_af_view_all_upcoming_trainings_btn(self, get_base_url, get_training_af_url):
        self.driver.get(get_training_af_url)
        af_view_all_upcoming_trainings_btn = TrainingLocator.get_af_view_all_upcoming_trainings_btn(self)
        af_view_all_upcoming_trainings_btn_url = get_base_url + self.CONST.get('VIEW_ALL_UPCOMING_TRAININGS_BTN')
        view_all_upcoming_trainings_title = self.TITLES.get('VIEW_ALL_UPCOMING_TRAININGS_TITLE')
        assert Utils.is_displayed(self,af_view_all_upcoming_trainings_btn), 'VIEW ALL UPCOMING TRAININGS BUTTON in Agile Framework page is not being displayed'
        path = Utils.click_link(self,af_view_all_upcoming_trainings_btn, view_all_upcoming_trainings_title, af_view_all_upcoming_trainings_btn_url) 
        assert path == af_view_all_upcoming_trainings_btn_url, 'VIEW ALL UPCOMING TRAININGS LINK in Agile Framework page is not working'

    #CUSTOM TRAINING INTO AGILE FRAMEWORK PAGE
    @allure.title("Test CUSTOM TRAINING LINK in Agile Framework page, is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_af_request_ct_btn
    def test_training_af_request_ct_btn(self, get_training_af_url):
        self.driver.get(get_training_af_url)
        af_request_cT_btn = TrainingLocator.get_af_request_ct_btn(self)  
        assert Utils.is_displayed(self,af_request_cT_btn), 'CUSTOM TRAINING LINK in Agile Framework page is not being displayed'
    
    #AGUILE CULTURE PAGE
    @allure.title("Test AGUILE CULTURE LINK redirect is working") 
    @allure.description(" Test if link redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_agile_culture_link
    def test_training_agile_culture_link(self, get_base_url):
        self.driver.get(get_base_url)
        training_link = HeaderLocator.get_training_link(self)
       # assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_culture_link = HeaderLocator.get_submenu_training(self)[2]
        agile_culture_url = get_base_url + self.CONSTHEADER.get('SUBMENU_AGILECULTURE')
        path = Utils.click_link(self,agile_culture_link, self.TITLES.get('AGILE_CULTURE_TITLE'),agile_culture_url) 
        assert path == agile_culture_url, 'AGILE CLULTURE link is not working'

    @allure.title("Test REQUEST TRAINING BUTTON in AGUILE CULTURE page, is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.training_ac_request_training_btn
    def test_training_ac_request_training_btn(self, get_base_url):
        ac_request_training_btn = TrainingLocator.get_ac_request_training_btn(self)
        ac_request_training_btn_url = get_base_url + self.CONST.get('CONTACTUS_REGISTER_BTN2')
        contactus_register_title = self.TITLES.get('CONTACTUS_REGISTER_TITLE')
        assert Utils.is_displayed(self,ac_request_training_btn), 'REQUEST CUSTOM TRAINING BUTTON in AGUILE CULTURE page is not being displayed'
        path = Utils.click_link(self,ac_request_training_btn, contactus_register_title, ac_request_training_btn_url) 
        assert path == ac_request_training_btn_url, 'REQUEST CUSTOM TRAINING LINK in AGUILE CULTURE page is not working'