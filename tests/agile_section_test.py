import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_locator import HomeLocator
from common.environment import CONSTANTS, PAGE_ELEMENTS
from common.utils import Utils


@pytest.mark.usefixtures("setup")
class TestAgileSection:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']
    ELEMENTS = PAGE_ELEMENTS['HOME']

    #AGILE PRACTICES AND TOOLS
       
    @allure.title("Test AGILE PRACTICES AND TOOLS LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_practices_and_tools_link
    def test_home_agile_practices_and_tools_link(self, get_base_url):
        agile_practices_and_tools_link = HomeLocator.get_agile_practices_and_tools_link(self)
        agile_practices_and_tools_link_url = get_base_url + self.CONST.get('AGILE_PRACTICES_AND_TOOLS_LINK')
        agile_practices_and_tools_title = self.TITLES.get('AGILE_PRACTICES_AND_TOOLS_TITLE')
        assert Utils.is_displayed(self,agile_practices_and_tools_link), 'AGILE PRACTICES AND TOOLS LINK is not being displayed'
        path = Utils.click_link(self,agile_practices_and_tools_link, agile_practices_and_tools_title, agile_practices_and_tools_link_url) 
        assert path == agile_practices_and_tools_link_url, 'AGILE PRACTICES AND TOOLS LINK is not working'
        
        
    @allure.title("Test BEHAVIOR DRIVEN DEVELOPMENT LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_bdd_link
    def test_home_bdd_link(self, get_base_url):
        self.driver.get(get_base_url)
        bdd_link = HomeLocator.get_bdd_link(self)
        bdd_link_url = get_base_url + self.CONST.get('BDD_LINK')
        bdd_title = self.TITLES.get('BDD_TITLE')
        assert Utils.is_displayed(self,bdd_link), 'BEHAVIOR DRIVEN DEVELOPMENT LINK is not being displayed'
        path = Utils.click_link(self,bdd_link, bdd_title, bdd_link_url) 
        assert path == bdd_link_url, 'BEHAVIOR DRIVEN DEVELOPMENT LINK is not working'
        
        
    @allure.title("Test BDD REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_bdd_btn
    def test_home_request_bdd_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_bdd_btn = HomeLocator.get_request_bdd_btn(self)   
        assert Utils.is_displayed(self,request_bdd_btn), 'BDD REGISTER BUTTON  is not being displayed'


    @allure.title("Test AGILE TESTING WORKSHOP LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_testing_workshop_link
    def test_home_agile_testing_workshop_link(self, get_base_url):
        agile_testing_workshop_link = HomeLocator.get_agile_testing_workshop_link(self)
        agile_testing_workshop_link_url = get_base_url + self.CONST.get('AGILE_TESTING_WORKSHOP_LINK')
        agile_testing_workshop_title = self.TITLES.get('AGILE_TESTING_WORKSHOP_TITLE')
        assert Utils.is_displayed(self,agile_testing_workshop_link), 'AGILE TESTING WORKSHOP LINK is not being displayed'
        path = Utils.click_link(self,agile_testing_workshop_link, agile_testing_workshop_title, agile_testing_workshop_link_url) 
        assert path == agile_testing_workshop_link_url, 'AGILE TESTING WORKSHOP LINK is not working'
        
        
    @allure.title("Test AGILE TESTING WORKSHOP REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_agiltesting_btn
    def test_home_request_agiltesting_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agiltesting_btn = HomeLocator.get_request_agiltesting_btn(self)  
        assert Utils.is_displayed(self,request_agiltesting_btn), 'AGILE TESTING WORKSHOP REGISTER is not being displayed'
       
    #AGILE CULTURE
       
    @allure.title("Test AGILE CULTURE LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_culture_link
    def test_home_agile_culture_link(self, get_base_url):
        agile_culture_link = HomeLocator.get_agile_culture_link(self)
        agile_culture_link_url = get_base_url + self.CONST.get('AGILE_CULTURE_LINK')
        agile_culture_title = self.TITLES.get('AGILE_CULTURE_TITLE')
        assert Utils.is_displayed(self,agile_culture_link), 'AGILE CULTURE LINK is not being displayed'
        path = Utils.click_link(self,agile_culture_link, agile_culture_title, agile_culture_link_url) 
        assert path == agile_culture_link_url, 'AGILE CULTURE LINK is not working'
        
        
    @allure.title("Test AGILE DIVERSITY LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_diversity_link
    def test_home_agile_diversity_link(self, get_base_url):
        self.driver.get(get_base_url)
        agile_diversity_link = HomeLocator.get_agile_diversity_link(self)
        agile_diversity_link_url = get_base_url + self.CONST.get('AGILE_DIVERSITY_LINK')
        agile_diversity_title = self.TITLES.get('AGILE_DIVERSITY_TITLE')
        assert Utils.is_displayed(self,agile_diversity_link), 'AGILE DIVERSITY LINK is not being displayed'
        path = Utils.click_link(self,agile_diversity_link, agile_diversity_title, agile_diversity_link_url) 
        assert path == agile_diversity_link_url, 'AGILE DIVERSITY LINK is not working'
        
        
    @allure.title("Test AGILE DIVERSITY REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_agildiverity_btn
    def test_home_request_agildiverity_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agildiverity_btn = HomeLocator.get_request_agildiverity_btn(self)  
        assert Utils.is_displayed(self,request_agildiverity_btn), 'AGILE DIVERSITY REGISTER is not being displayed'
       
       
    @allure.title("Test AGILE CONFLICT LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_conflict_link
    def test_home_agile_conflict_link(self, get_base_url):
        agile_conflict_link = HomeLocator.get_agile_conflict_link(self)
        agile_conflict_link_url = get_base_url + self.CONST.get('AGILE_CONFLICT_LINK')
        agile_conflict_title = self.TITLES.get('AGILE_CONFLICT_TITLE')
        assert Utils.is_displayed(self,agile_conflict_link), 'AGILE CONFLICT LINK is not being displayed'
        path = Utils.click_link(self,agile_conflict_link, agile_conflict_title, agile_conflict_link_url) 
        assert path == agile_conflict_link_url, 'AGILE CONFLICT LINK is not working'
        
        
    @allure.title("Test AGILE CONFLICT REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_agilconflict_btn
    def test_home_request_agilconflict_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilconflict_btn = HomeLocator.get_request_agilconflict_btn(self)  
        assert Utils.is_displayed(self,request_agilconflict_btn), 'AGILE CONFLICT REGISTER is not being displayed'
        
        
    @allure.title("Test AGILE MOTIVATION LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_motivation_link
    def test_home_agile_motivation_link(self, get_base_url):
        agile_motivation_link = HomeLocator.get_agile_motivation_link(self)
        agile_motivation_link_url = get_base_url + self.CONST.get('AGILE_MOTIVATION_LINK')
        agile_motivation_title = self.TITLES.get('AGILE_MOTIVATION_TITLE')
        assert Utils.is_displayed(self,agile_motivation_link), 'AGILE MOTIVATION LINK is not being displayed'
        path = Utils.click_link(self,agile_motivation_link, agile_motivation_title, agile_motivation_link_url) 
        assert path == agile_motivation_link_url, 'AGILE MOTIVATION LINK is not working'
        
        
    @allure.title("Test AGILE MOTIVATION REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_agilmotivation_btn
    def test_home_request_agilmotivation_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilmotivation_btn = HomeLocator.get_request_agilmotivation_btn(self)  
        assert Utils.is_displayed(self,request_agilmotivation_btn), 'AGILE MOTIVATION REQUEST BUTTON is not being displayed'
        
        
    @allure.title("Test AGILE CHANGE LINK is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_change_link
    def test_home_agile_change_link(self, get_base_url):
        agile_change_link = HomeLocator.get_agile_change_link(self)
        agile_change_link_url = get_base_url + self.CONST.get('AGILE_CHANGE_LINK')
        agile_change_title = self.TITLES.get('AGILE_CHANGE_TITLE')
        assert Utils.is_displayed(self,agile_change_link), 'AGILE CHANGE LINK is not being displayed'
        path = Utils.click_link(self,agile_change_link, agile_change_title, agile_change_link_url) 
        assert path == agile_change_link_url, 'AGILE CHANGE LINK is not working'
        
        
    @allure.title("Test AGILE CHANGE REQUEST BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_agilchanges_btn
    def test_home_request_agilchanges_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilchanges_btn = HomeLocator.get_request_agilchanges_btn(self)  
        assert Utils.is_displayed(self,request_agilchanges_btn), 'AGILE CHANGE REQUEST BUTTON is not being displayed'  