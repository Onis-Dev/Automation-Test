import pytest
import allure
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.environment import CONSTANTS

@pytest.mark.usefixtures("setup")
class TestHeader:

    CONST = CONSTANTS['header']

    def test_logo_smoothapps(self):
        logo = self.driver.find_element(By.ID,'logo').is_displayed()
        assert logo, 'Logo smoothapps is not being displayed'

    def test_header_home_link(self):
        home_link = self.driver.find_element(By.ID, 'menu-item-5121')
        assert home_link.is_displayed(), 'HOME link is not being displayed'
        path = self.clickEvent(home_link,self.CONST.get('HOME_LINK'))
        assert path == self.CONST.get('HOME_LINK'), 'HOME link is not working'
    
    #util methods | Start
    def getTrainingLink(self):
        return self.driver.find_element(By.ID, 'menu-item-7212')
    
    def getSubmenuTraining(self):
        return (self.driver.find_element(By.ID, 'menu-item-5151'),
               self.driver.find_element(By.ID, 'menu-item-8080'),
               self.driver.find_element(By.ID, 'menu-item-5152'))
    
    def clickEvent(self, element, page):
        element.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(page))
        return self.driver.current_url

    def getAboutLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5580')
    
    def getSubmenuAbout(self):
        return (self.driver.find_element(By.ID, 'menu-item-5168'),
               self.driver.find_element(By.ID, 'menu-item-5169'),
               self.driver.find_element(By.ID, 'menu-item-4706'),
               self.driver.find_element(By.ID, 'menu-item-7943'))

    def getResourcesLink(self):
        return self.driver.find_element(By.ID, 'menu-item-5581')
    
    def getSubmenuResources(self):
        return (self.driver.find_element(By.ID, 'menu-item-7771'),
               self.driver.find_element(By.ID, 'menu-item-5171'),
               self.driver.find_element(By.ID, 'menu-item-5176'),
               self.driver.find_element(By.ID, 'menu-item-5172'))
    #util methods | END

    def test_header_training_link(self):
        training_link = self.getTrainingLink()
        assert training_link.is_displayed(), 'TRAINING link is not being displayed'
        path = self.clickEvent(training_link, self.CONST.get('TRAINING_LINK')) 
        assert path == self.CONST.get('TRAINING_LINK'), 'TRAINING link is not working'
    
    def test_header_trianing_submenu(self):
        training_link = self.getTrainingLink()
        actions =chains(self.driver)
        actions.move_to_element(training_link).perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-7212 > ul')))
        agile_framework_link, agile_practices_link, agile_culture_link = self.getSubmenuTraining()
        assert agile_framework_link.is_displayed(), 'submenu AGILE FRAMEWORK is not being displayed'
        assert agile_practices_link.is_displayed(), 'submenu AGILE PRACTICES is not being displayed'
        assert agile_culture_link.is_displayed(), 'submenu AGILE CULTURE is not being displayed'

    def test_header_training_submenu_agileFramework_redirect(self):
        training_link = self.getTrainingLink()
        actions =chains(self.driver)
        actions.move_to_element(training_link).perform()
        agile_framework_link = self.getSubmenuTraining()[0]
        path = self.clickEvent(agile_framework_link, self.CONST.get('SUBMENU_AGILEFRAMEWORK'))
        assert path == self.CONST.get('SUBMENU_AGILEFRAMEWORK'), 'submenu AGILE FRAMEWORK link is not working'

    def test_header_training_submenu_agilepractices_redirect(self):
        training_link = self.getTrainingLink()
        actions =chains(self.driver)
        actions.move_to_element(training_link).perform()
        agile_practices_link = self.getSubmenuTraining()[1]
        path = self.clickEvent(agile_practices_link, self.CONST.get('SUBMENU_AGILEPRACTICES_TOOLS'))
        assert path == self.CONST.get('SUBMENU_AGILEPRACTICES_TOOLS'), 'submenu AGILE PRACTICES and tools link is not working'
    
    def test_header_training_submenu_agileCulture_redirect(self):
        training_link = self.getTrainingLink()
        actions =chains(self.driver)
        actions.move_to_element(training_link).perform()
        agile_culture_link = self.getSubmenuTraining()[2]
        path = self.clickEvent(agile_culture_link, self.CONST.get('SUBMENU_AGILECULTURE'))
        assert path == self.CONST.get('SUBMENU_AGILECULTURE'), 'submenu AGILE CULTURE link is not working'

    def test_header_services_link(self):
        services_link = self.driver.find_element(By.ID, 'menu-item-5598')
        assert services_link.is_displayed(), 'SERVICES link is not being displayed'
        path = self.clickEvent(services_link, self.CONST.get('SERVICES_LINK'))
        assert path == self.CONST.get('SERVICES_LINK'), 'SERVICES link is not working'
    
    def test_header_events_link(self):
        events_link = self.driver.find_element(By.ID, 'menu-item-5174')
        assert events_link.is_displayed(), 'EVENTS link is not being displayed'
        path = self.clickEvent(events_link, self.CONST.get('EVENTS_LINK'))
        assert path == self.CONST.get('EVENTS_LINK'), 'EVENTS link is not working'

    def test_header_about_link(self):
        about_link = self.getAboutLink()
        assert about_link.is_displayed(), 'ABOUT link is not being displayed'

    def test_header_about_submenu(self):
        about_link = self.getAboutLink()
        actions =chains(self.driver)
        actions.move_to_element(about_link).perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5580 > ul')))
        company_link, partners_link, testimonials_link, careers_link = self.getSubmenuAbout()
        assert company_link.is_displayed(), 'submenu COMPANY is not being displayed'
        assert partners_link.is_displayed(), 'submenu PARTNERS is not being displayed'
        assert testimonials_link.is_displayed(), 'submenu TESTIMONIALS is not being displayed'
        assert careers_link.is_displayed(), 'submenu CAREERS is not being displayed'
    
    def test_header_about_submenu_company_redirect(self):
        about_link = self.getAboutLink()
        actions =chains(self.driver)
        actions.move_to_element(about_link).perform()
        company_link = self.getSubmenuAbout()[0]
        path = self.clickEvent(company_link, self.CONST.get('SUBMENU_COMPANY'))
        assert path == self.CONST.get('SUBMENU_COMPANY'), 'submenu COMPANY link is not working'
    
    def test_header_about_submenu_partners_redirect(self):
        about_link = self.getAboutLink()
        actions =chains(self.driver)
        actions.move_to_element(about_link).perform()
        partners_link = self.getSubmenuAbout()[1]
        path = self.clickEvent(partners_link, self.CONST.get('SUBMENU_PARTNERS'))
        assert path == self.CONST.get('SUBMENU_PARTNERS'), 'submenu PARTNERS link is not working'
    
    def test_header_about_submenu_testimonial_redirect(self):
        about_link = self.getAboutLink()
        actions =chains(self.driver)
        actions.move_to_element(about_link).perform()
        testimonial_link = self.getSubmenuAbout()[2]
        path = self.clickEvent(testimonial_link, self.CONST.get('SUBMENU_TESTIMONIALS'))
        assert path == self.CONST.get('SUBMENU_TESTIMONIALS'), 'submenu TESTIMONIALS link is not working'
    
    def test_header_about_submenu_careers_redirect(self):
        about_link = self.getAboutLink()
        actions =chains(self.driver)
        actions.move_to_element(about_link).perform()
        careers_link = self.getSubmenuAbout()[3]
        path = self.clickEvent(careers_link, self.CONST.get('SUBMENU_CAREERS'))
        assert path == self.CONST.get('SUBMENU_CAREERS'), 'submenu CAREERS link is not working'
    
    def test_header_resources_link(self):
        resources_link = self.getResourcesLink()
        assert resources_link.is_displayed(), 'RESOURCES link is not being displayed'

    def test_header_resources_submenu(self):
        resources_link = self.getResourcesLink()
        actions =chains(self.driver)
        actions.move_to_element(resources_link).perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#menu-item-5581 > ul')))
        scrum_events_link, agile_videos_link, agile_presentations_link, agile_tools_link = self.getSubmenuResources()
        assert scrum_events_link.is_displayed(), 'submenu SCRUM EVENTS PLAYBOOK is not being displayed'
        assert agile_videos_link.is_displayed(), 'submenu AGILE VIDEOS is not being displayed'
        assert agile_presentations_link.is_displayed(), 'submenu AGILE PRESENTATIONS is not being displayed'
        assert agile_tools_link.is_displayed(), 'submenu AGILE TOOLS is not being displayed'
    
    def test_header_resources_submenu_scrumEvents_redirect(self):
        resources_link = self.getResourcesLink()
        actions =chains(self.driver)
        actions.move_to_element(resources_link).perform()
        scrum_events_link = self.getSubmenuResources()[0]
        path = self.clickEvent(scrum_events_link, self.CONST.get('SUBMENU_SCRUM_EVENTS'))
        assert path == self.CONST.get('SUBMENU_SCRUM_EVENTS'), 'submenu SCRUM EVENTS PLAYBOOK link is not working'
    
    def test_header_resources_submenu_agileVideos_redirect(self):
        resources_link = self.getResourcesLink()
        actions =chains(self.driver)
        actions.move_to_element(resources_link).perform()
        agile_videos_link = self.getSubmenuResources()[1]
        path = self.clickEvent(agile_videos_link, self.CONST.get('SUBMENU_AGILE_VIDEOS'))
        assert path == self.CONST.get('SUBMENU_AGILE_VIDEOS'), 'submenu AGILE VIDEOS link is not working'

    def test_header_resources_submenu_agilePresentation_redirect(self):
        resources_link = self.getResourcesLink()
        actions =chains(self.driver)
        actions.move_to_element(resources_link).perform()
        agile_presentations_link = self.getSubmenuResources()[2]
        path = self.clickEvent(agile_presentations_link, self.CONST.get('SUBMENU_AGILE_PRESENTATIONS'))
        assert path == self.CONST.get('SUBMENU_AGILE_PRESENTATIONS'), 'submenu AGILE PRESENTATIONS link is not working'  

    def test_header_resources_submenu_agileTools_redirect(self):
        resources_link = self.getResourcesLink()
        actions =chains(self.driver)
        actions.move_to_element(resources_link).perform()
        agile_tools_link = self.getSubmenuResources()[3]
        
        path = self.clickEvent(agile_tools_link, self.CONST.get('SUBMENU_AGILE_TOOLS'))
        assert path == self.CONST.get('SUBMENU_AGILE_TOOLS'), 'submenu AGILE TOOLS link is not working' 
    
    def test_header_blog_link(self):
        blog_link = self.driver.find_element(By.ID, 'menu-item-5173')
        assert blog_link.is_displayed(), 'BLOG link is not being displayed'
        path = self.clickEvent(blog_link, self.CONST.get('BLOG_LINK')) 
        assert path == self.CONST.get('BLOG_LINK'), 'BLOG link is not working'