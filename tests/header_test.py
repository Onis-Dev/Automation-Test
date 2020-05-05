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
@allure.title("All header tests")
class TestHeader:

    CONST = CONSTANTS['header']
    @allure.title("Test logo 'Smoothapps'")
    @allure.description(" Test if logo is displayed")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.header_logo
    def test_logo_smoothapps(self):
        logo = Utils.is_displayed(self,HeaderLocator.getLogo(self))
        assert logo, 'Logo smoothapps is not being displayed'

    @allure.title("Test HOME LINK redirect is displayed and working")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_home_link
    def test_header_home_link(self):
        home_link = HeaderLocator.getHomeLink(self)
        assert Utils.is_displayed(self,home_link), 'HOME link is not being displayed'
        path = Utils.clickLink(self,home_link,self.CONST.get('HOME_LINK'))
        assert path == self.CONST.get('HOME_LINK'), 'HOME link is not working'

    @allure.title("Test TRAINING LINK redirect is displayed and working")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_training_link
    def test_header_training_link(self):
        training_link = HeaderLocator.getTrainingLink(self)
        assert Utils.is_displayed(self,training_link), 'TRAINING link is not being displayed'
        path = Utils.clickLink(self,training_link, self.CONST.get('TRAINING_LINK')) 
        assert path == self.CONST.get('TRAINING_LINK'), 'TRAINING link is not working'
    
    @allure.title("Test TRAINING SUBMENU LINKS items are displayed")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.header_training_submenu
    def test_header_trianing_submenu(self):
        training_link = HeaderLocator.getTrainingLink(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-7212 > ul')))
        agile_framework_link, agile_practices_link, agile_culture_link = HeaderLocator.getSubmenuTraining(self)
        assert Utils.is_displayed(self,agile_framework_link), 'submenu AGILE FRAMEWORK is not being displayed'
        assert Utils.is_displayed(self,agile_practices_link), 'submenu AGILE PRACTICES is not being displayed'
        assert Utils.is_displayed(self,agile_culture_link), 'submenu AGILE CULTURE is not being displayed'
    
    @allure.title("Test AGILE FRAMEWORK link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileFramework_link
    def test_header_training_submenu_agileFramework_redirect(self):
        training_link = HeaderLocator.getTrainingLink(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_framework_link = HeaderLocator.getSubmenuTraining(self)[0]
        path = Utils.clickLink(self,agile_framework_link, self.CONST.get('SUBMENU_AGILEFRAMEWORK'))
        assert path == self.CONST.get('SUBMENU_AGILEFRAMEWORK'), 'submenu AGILE FRAMEWORK link is not working'

    @allure.title("Test AGILE PRACTICES and TOOLS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agilePractices_link
    def test_header_training_submenu_agilepractices_redirect(self):
        training_link = HeaderLocator.getTrainingLink(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_practices_link = HeaderLocator.getSubmenuTraining(self)[1]
        path = Utils.clickLink(self,agile_practices_link, self.CONST.get('SUBMENU_AGILEPRACTICES_TOOLS'))
        assert path == self.CONST.get('SUBMENU_AGILEPRACTICES_TOOLS'), 'submenu AGILE PRACTICES and TOOLS link is not working'
    
    @allure.title("Test AGILE CULTURE link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileCulture_link
    def test_header_training_submenu_agileCulture_redirect(self):
        training_link = HeaderLocator.getTrainingLink(self)
        assert Utils.is_displayed(self,training_link), "Can't find link element"
        Utils.hover_on_link(self,training_link)
        agile_culture_link = HeaderLocator.getSubmenuTraining(self)[2]
        path = Utils.clickLink(self,agile_culture_link, self.CONST.get('SUBMENU_AGILECULTURE'))
        assert path == self.CONST.get('SUBMENU_AGILECULTURE'), 'submenu AGILE CULTURE link is not working'

    @allure.title("Test SERVICES link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_services_link
    def test_header_services_link(self):
        services_link = HeaderLocator.getServicesLink(self)
        assert Utils.is_displayed(self,services_link), 'SERVICES link is not being displayed'
        path = Utils.clickLink(self,services_link, self.CONST.get('SERVICES_LINK'))
        assert path == self.CONST.get('SERVICES_LINK'), 'SERVICES link is not working'
    
    @allure.title("Test EVENTS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_events_link
    def test_header_events_link(self):
        events_link = HeaderLocator.getEventslink(self)
        assert Utils.is_displayed(self,events_link), 'EVENTS link is not being displayed'
        path = Utils.clickLink(self,events_link, self.CONST.get('EVENTS_LINK'))
        assert path == self.CONST.get('EVENTS_LINK'), 'EVENTS link is not working'

    @allure.title("Test ABOUT link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_about_link
    def test_header_about_link(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), 'ABOUT link is not being displayed'

    @allure.title("Test ABOUT SUBMENU LINKS are displayed")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_about_submenu
    def test_header_about_submenu(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5580 > ul')))
        company_link, partners_link, testimonials_link, careers_link = HeaderLocator.getSubmenuAbout(self)
        assert Utils.is_displayed(self,company_link), 'submenu COMPANY is not being displayed'
        assert Utils.is_displayed(self,partners_link), 'submenu PARTNERS is not being displayed'
        assert Utils.is_displayed(self,testimonials_link), 'submenu TESTIMONIALS is not being displayed'
        assert Utils.is_displayed(self,careers_link), 'submenu CAREERS is not being displayed'

    @allure.title("Test ABOUT SUBMENU COMPANY link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_company_link
    def test_header_about_submenu_company_redirect(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        company_link = HeaderLocator.getSubmenuAbout(self)[0]
        path = Utils.clickLink(self,company_link, self.CONST.get('SUBMENU_COMPANY'))
        assert path == self.CONST.get('SUBMENU_COMPANY'), 'submenu COMPANY link is not working'

    @allure.title("Test ABOUT SUBMENU PARTNERS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_partners_link
    def test_header_about_submenu_partners_redirect(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        partners_link = HeaderLocator.getSubmenuAbout(self)[1]
        path = Utils.clickLink(self,partners_link, self.CONST.get('SUBMENU_PARTNERS'))
        assert path == self.CONST.get('SUBMENU_PARTNERS'), 'submenu PARTNERS link is not working'

    @allure.title("Test ABOUT SUBMENU TESTIMONIALS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_testimonials_link
    def test_header_about_submenu_testimonial_redirect(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        testimonial_link = HeaderLocator.getSubmenuAbout(self)[2]
        path = Utils.clickLink(self,testimonial_link, self.CONST.get('SUBMENU_TESTIMONIALS'))
        assert path == self.CONST.get('SUBMENU_TESTIMONIALS'), 'submenu TESTIMONIALS link is not working'

    @allure.title("Test ABOUT SUBMENU CAREERS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_careers_link
    def test_header_about_submenu_careers_redirect(self):
        about_link = HeaderLocator.getAboutLink(self)
        assert Utils.is_displayed(self,about_link), "Can't find link element"
        Utils.hover_on_link(self,about_link)
        careers_link = HeaderLocator.getSubmenuAbout(self)[3]
        path = Utils.clickLink(self,careers_link, self.CONST.get('SUBMENU_CAREERS'))
        assert path == self.CONST.get('SUBMENU_CAREERS'), 'submenu CAREERS link is not working'

    @allure.title("Test RESOURCES is displayed")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_resources_link
    def test_header_resources_link(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), 'RESOURCES link is not being displayed'

    @allure.title("Test SUBMENU RESOURCES is displayed")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_resources_submenu
    def test_header_resources_submenu(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5581 > ul')))
        scrum_events_link, agile_videos_link, agile_presentations_link, agile_tools_link = HeaderLocator.getSubmenuResources(self)
        assert Utils.is_displayed(self,scrum_events_link), 'submenu SCRUM EVENTS PLAYBOOK is not being displayed'
        assert Utils.is_displayed(self,agile_videos_link), 'submenu AGILE VIDEOS is not being displayed'
        assert Utils.is_displayed(self,agile_presentations_link), 'submenu AGILE PRESENTATIONS is not being displayed'
        assert Utils.is_displayed(self,agile_tools_link), 'submenu AGILE TOOLS is not being displayed'

    @allure.title("Test SCRUM EVENTS PLAYBOOK link redirect")
    @allure.description(" Test if link is displayed and working")    
    def test_header_resources_submenu_scrumEvents_redirect(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        scrum_events_link = HeaderLocator.getSubmenuResources(self)[0]
        path = Utils.clickLink(self,scrum_events_link, self.CONST.get('SUBMENU_SCRUM_EVENTS'))
        assert path == self.CONST.get('SUBMENU_SCRUM_EVENTS'), 'submenu SCRUM EVENTS PLAYBOOK link is not working'

    @allure.title("Test AGILE VIDEOS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileVideos_link
    def test_header_resources_submenu_agileVideos_redirect(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_videos_link = HeaderLocator.getSubmenuResources(self)[1]
        path = Utils.clickLink(self,agile_videos_link, self.CONST.get('SUBMENU_AGILE_VIDEOS'))
        assert path == self.CONST.get('SUBMENU_AGILE_VIDEOS'), 'submenu AGILE VIDEOS link is not working'

    @allure.title("Test AGILE PRESENTATIONS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agilePresentations_link
    def test_header_resources_submenu_agilePresentation_redirect(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_presentations_link = HeaderLocator.getSubmenuResources(self)[2]
        path = Utils.clickLink(self,agile_presentations_link, self.CONST.get('SUBMENU_AGILE_PRESENTATIONS'))
        assert path == self.CONST.get('SUBMENU_AGILE_PRESENTATIONS'), 'submenu AGILE PRESENTATIONS link is not working'  

    @allure.title("Test AGILE TOOLS link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_agileTools_link
    def test_header_resources_submenu_agileTools_redirect(self):
        resources_link = HeaderLocator.getResourcesLink(self)
        assert Utils.is_displayed(self,resources_link), "Can't find link element"
        Utils.hover_on_link(self,resources_link)
        agile_tools_link = HeaderLocator.getSubmenuResources(self)[3]
        path = Utils.clickLink(self,agile_tools_link, self.CONST.get('SUBMENU_AGILE_TOOLS'))
        assert path == self.CONST.get('SUBMENU_AGILE_TOOLS'), 'submenu AGILE TOOLS link is not working' 
    
    @allure.title("Test BLOG link redirect")
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.header_blog_link
    def test_header_blog_link(self):
        blog_link = HeaderLocator.getBlogLink(self)
        assert Utils.is_displayed(self,blog_link), 'BLOG link is not being displayed'
        path = Utils.clickLink(self,blog_link, self.CONST.get('BLOG_LINK')) 
        assert path == self.CONST.get('BLOG_LINK'), 'BLOG link is not working'