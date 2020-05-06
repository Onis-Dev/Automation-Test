import pytest
import allure
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.header_locator import HeaderLocator
from common.environment import CONSTANTS
from common.utils import Utils

@pytest.mark.usefixtures("setup")
@allure.description("This class contains all header test cases")
class TestHeader:

    """ Read all constants from header section"""
    CONST = CONSTANTS['header']

    @allure.title("Test HOME LINK redirect is displayed and working")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_home_link
    def test_header_home_link(self, get_base_url):
        home_link = HeaderLocator.get_home_link(self)
        assert Utils.is_displayed(self,home_link), 'HOME link is not being displayed'
        path = Utils.click_link(self,home_link,get_base_url)
        assert path == get_base_url, 'HOME link is not working'

    @allure.title("Test TRAINING LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_training_link
    def test_header_training_link(self, get_base_url):
        training_link = HeaderLocator.get_training_link(self)
        training_url = get_base_url + self.CONST.get('TRAINING_LINK')
        assert Utils.is_displayed(self,training_link), 'TRAINING link is not being displayed'
        path = Utils.click_link(self,training_link, training_url) 
        assert path == training_url, 'TRAINING link is not working'
    
    @allure.title("Test TRAINING SUBMENU LINKS are displayed")
    @allure.description("Test if Submenu links are being displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.header_training_submenu
    def test_header_trianing_submenu(self):
        training_link = HeaderLocator.get_training_link(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-7212 > ul')))
        agile_framework_link, agile_practices_link, agile_culture_link = HeaderLocator.get_submenu_training(self)
        assert Utils.is_displayed(self,agile_framework_link), 'submenu AGILE FRAMEWORK is not being displayed'
        assert Utils.is_displayed(self,agile_practices_link), 'submenu AGILE PRACTICES is not being displayed'
        assert Utils.is_displayed(self,agile_culture_link), 'submenu AGILE CULTURE is not being displayed'
    
    @allure.title("Test AGILE FRAMEWORK link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileFramework_link
    def test_header_training_submenu_agileFramework_redirect(self, get_base_url):
        training_link = HeaderLocator.get_training_link(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_framework_link = HeaderLocator.get_submenu_training(self)[0]
        agile_framework_path = get_base_url + self.CONST.get('SUBMENU_AGILEFRAMEWORK')
        path = Utils.click_link(self,agile_framework_link, agile_framework_path)
        assert path == agile_framework_path, 'submenu AGILE FRAMEWORK link is not working'

    @allure.title("Test AGILE PRACTICES and TOOLS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agilePractices_link
    def test_header_training_submenu_agilepractices_redirect(self, get_base_url):
        training_link = HeaderLocator.get_training_link(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_practices_link = HeaderLocator.get_submenu_training(self)[1]
        agile_practices_path = get_base_url + self.CONST.get('SUBMENU_AGILEPRACTICES_TOOLS')
        path = Utils.click_link(self,agile_practices_link, agile_practices_path)
        assert path == agile_practices_path, 'submenu AGILE PRACTICES and TOOLS link is not working'
    
    @allure.title("Test AGILE CULTURE link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileCulture_link
    def test_header_training_submenu_agileCulture_redirect(self, get_base_url):
        training_link = HeaderLocator.get_training_link(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_culture_link = HeaderLocator.get_submenu_training(self)[2]
        agile_culture_path = get_base_url + self.CONST.get('SUBMENU_AGILECULTURE')
        path = Utils.click_link(self,agile_culture_link, agile_culture_path)
        assert path == agile_culture_path, 'submenu AGILE CULTURE link is not working'

    @allure.title("Test SERVICES link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_services_link
    def test_header_services_link(self, get_base_url):
        services_link = HeaderLocator.get_services_link(self)
        assert Utils.is_displayed(self,services_link), 'SERVICES link is not being displayed'
        services_full_path = get_base_url + self.CONST.get('SERVICES_LINK')
        path = Utils.click_link(self,services_link, services_full_path )
        assert path == services_full_path, 'SERVICES link is not working'
    
    @allure.title("Test EVENTS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_events_link
    def test_header_events_link(self, get_base_url):
        events_link = HeaderLocator.get_events_link(self)
        assert Utils.is_displayed(self,events_link), 'EVENTS link is not being displayed'
        events_path = get_base_url + self.CONST.get('EVENTS_LINK')
        path = Utils.click_link(self,events_link, events_path)
        assert path == events_path, 'EVENTS link is not working'

    @allure.title("Test ABOUT link is being displayed")
    @allure.description(" Test if about link is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_about_link
    def test_header_about_link(self):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), 'ABOUT link is not being displayed'

    @allure.title("Test ABOUT SUBMENU LINKS are displayed")
    @allure.description(" Test if submenu links are being displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_about_submenu
    def test_header_about_submenu(self):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5580 > ul')))
        company_link, partners_link, testimonials_link, careers_link = HeaderLocator.get_submenu_about(self)
        assert Utils.is_displayed(self,company_link), 'submenu COMPANY is not being displayed'
        assert Utils.is_displayed(self,partners_link), 'submenu PARTNERS is not being displayed'
        assert Utils.is_displayed(self,testimonials_link), 'submenu TESTIMONIALS is not being displayed'
        assert Utils.is_displayed(self,careers_link), 'submenu CAREERS is not being displayed'

    @allure.title("Test ABOUT SUBMENU COMPANY link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_company_link
    def test_header_about_submenu_company_redirect(self, get_base_url):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        company_link = HeaderLocator.get_submenu_about(self)[0]
        company_path = get_base_url + self.CONST.get('SUBMENU_COMPANY')
        path = Utils.click_link(self,company_link, company_path)
        assert path == company_path, 'submenu COMPANY link is not working'

    @allure.title("Test ABOUT SUBMENU PARTNERS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_partners_link
    def test_header_about_submenu_partners_redirect(self, get_base_url):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        partners_link = HeaderLocator.get_submenu_about(self)[1]
        partners_path = get_base_url + self.CONST.get('SUBMENU_PARTNERS')
        path = Utils.click_link(self,partners_link, partners_path)
        assert path == partners_path, 'submenu PARTNERS link is not working'

    @allure.title("Test ABOUT SUBMENU TESTIMONIALS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_testimonials_link
    def test_header_about_submenu_testimonial_redirect(self, get_base_url):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        testimonial_link = HeaderLocator.get_submenu_about(self)[2]
        testimonials_path = get_base_url + self.CONST.get('SUBMENU_TESTIMONIALS')
        path = Utils.click_link(self,testimonial_link, testimonials_path)
        assert path == testimonials_path, 'submenu TESTIMONIALS link is not working'

    @allure.title("Test ABOUT SUBMENU CAREERS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_careers_link
    def test_header_about_submenu_careers_redirect(self, get_base_url):
        about_link = HeaderLocator.get_about_link(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        careers_link = HeaderLocator.get_submenu_about(self)[3]
        careers_path = get_base_url + self.CONST.get('SUBMENU_CAREERS')
        path = Utils.click_link(self,careers_link, careers_path)
        assert path == careers_path, 'submenu CAREERS link is not working'

    @allure.title("Test RESOURCES is displayed")
    @allure.description(" Test if link is being displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_resources_link
    def test_header_resources_link(self):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), 'RESOURCES link is not being displayed'

    @allure.title("Test SUBMENU RESOURCES is displayed")
    @allure.description(" Test if submenu links are being displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_resources_submenu
    def test_header_resources_submenu(self):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5581 > ul')))
        scrum_events_link, agile_videos_link, agile_presentations_link, agile_tools_link = HeaderLocator.get_submenu_resources(self)
        assert Utils.is_displayed(self,scrum_events_link), 'submenu SCRUM EVENTS PLAYBOOK is not being displayed'
        assert Utils.is_displayed(self,agile_videos_link), 'submenu AGILE VIDEOS is not being displayed'
        assert Utils.is_displayed(self,agile_presentations_link), 'submenu AGILE PRESENTATIONS is not being displayed'
        assert Utils.is_displayed(self,agile_tools_link), 'submenu AGILE TOOLS is not being displayed'

    @allure.title("Test SCRUM EVENTS PLAYBOOK link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")   
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_scrumEvents_link 
    def test_header_resources_submenu_scrumEvents_redirect(self, get_base_url):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        scrum_events_link = HeaderLocator.get_submenu_resources(self)[0]
        resources_path = get_base_url + self.CONST.get('SUBMENU_SCRUM_EVENTS')
        path = Utils.click_link(self,scrum_events_link, resources_path)
        assert path == resources_path, 'submenu SCRUM EVENTS PLAYBOOK link is not working'

    @allure.title("Test AGILE VIDEOS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileVideos_link
    def test_header_resources_submenu_agileVideos_redirect(self, get_base_url):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_videos_link = HeaderLocator.get_submenu_resources(self)[1]
        agile_videos_path = get_base_url + self.CONST.get('SUBMENU_AGILE_VIDEOS')
        path = Utils.click_link(self,agile_videos_link, agile_videos_path)
        assert path == agile_videos_path, 'submenu AGILE VIDEOS link is not working'

    @allure.title("Test AGILE PRESENTATIONS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agilePresentations_link
    def test_header_resources_submenu_agilePresentation_redirect(self, get_base_url):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_presentations_link = HeaderLocator.get_submenu_resources(self)[2]
        agile_presentations_path = get_base_url + self.CONST.get('SUBMENU_AGILE_PRESENTATIONS')
        path = Utils.click_link(self,agile_presentations_link, agile_presentations_path)
        assert path == agile_presentations_path, 'submenu AGILE PRESENTATIONS link is not working'  

    @allure.title("Test AGILE TOOLS link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileTools_link
    def test_header_resources_submenu_agileTools_redirect(self, get_base_url):
        resources_link = HeaderLocator.get_resources_link(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_tools_link = HeaderLocator.get_submenu_resources(self)[3]
        agile_tools_path = get_base_url + self.CONST.get('SUBMENU_AGILE_TOOLS')
        path = Utils.click_link(self,agile_tools_link, agile_tools_path)
        assert path == agile_tools_path, 'submenu AGILE TOOLS link is not working' 
    
    @allure.title("Test BLOG link redirect")
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_blog_link
    def test_header_blog_link(self, get_base_url):
        blog_link = HeaderLocator.get_blog_link(self)
        assert Utils.is_displayed(self,blog_link), 'BLOG link is not being displayed'
        blog_path = get_base_url + self.CONST.get('BLOG_LINK')
        path = Utils.click_link(self,blog_link, blog_path) 
        assert path == blog_path, 'BLOG link is not working'