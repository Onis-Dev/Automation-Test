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
class TestHome:

    CONST = CONSTANTS['HOME']
    #Learn More
    @allure.title("Test Learn More button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_training_link
    def test_learn_more_redirect(self, get_base_url):
        learn_more_btn = HomeLocator.getLearnMoreBtn(self)
        learn_more_url = get_base_url + self.CONST.get('LEARN_MORE_REDIRECT')
        assert Utils.is_displayed(self,learn_more_btn), 'Learn More button is no being displayed'
        path = Utils.click_link(self,learn_more_btn, learn_more_url) 
        assert path == learn_more_url, 'LEARN MORE REDIRECT is not working'
    
    #UPCOMING TRAININGS
    # PSPO
    @allure.title("Test PSPO link redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_pspo_link
    def test_home_pspo_link(self, get_base_url):
        self.driver.get(get_base_url)
        pspo_link = HomeLocator.getPspoLink(self)
        pspo_link_url = get_base_url + self.CONST.get('PSPO_LINK')
        assert Utils.is_displayed(self,pspo_link), 'PSPO LINK is not being displayed'
        path = Utils.click_link(self,pspo_link, pspo_link_url) 
        assert path == pspo_link_url, 'PSPO_LINK is not working'

    @allure.title("Test PSPO REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_pspo_register_link
    def test_home_pspo_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        pspo_register_link = HomeLocator.getPspoRegisterLink(self)
        pspo_register_link_url = self.CONST.get('PSPO_REGISTER_LINK')
        assert Utils.is_displayed(self,pspo_register_link), 'PSPO REGISTER button is not being displayed'
        path = Utils.click_link(self,pspo_register_link, pspo_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == pspo_register_link_url, 'PSPO REGISTER Link is not working'


    #PSM
    @allure.title("Test PSM  link, redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_psm_link
    def test_home_psm_link(self, get_base_url):
        psm_link = HomeLocator.getPsmLink(self)
        psm_link_url = get_base_url + self.CONST.get('PSM_LINK')
        assert Utils.is_displayed(self,psm_link), 'PSM LINK  is not being displayed'
        path = Utils.click_link(self,psm_link, psm_link_url) 
        assert path == psm_link_url, 'PSM LINK is not working'

    @allure.title("Test PSM REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_psm_register_link
    def test_home_psm_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        psm_register_link = HomeLocator.getPsmRegisterLink(self)
        psm_register_link_url = self.CONST.get('PSM_REGISTER_LINK')
        assert Utils.is_displayed(self,psm_register_link), 'PSM REGISTER button is not being displayed'
        path = Utils.click_link(self,psm_register_link, psm_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == psm_register_link_url, 'PSM REGISTER Link is not working'

    # SPS
    @allure.title("Test SPS link redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_sps_link
    def test_home_sps_link(self, get_base_url):
        sps_link = HomeLocator.getSpsLink(self)
        sps_link_url = get_base_url + self.CONST.get('SPS_LINK')
        assert Utils.is_displayed(self,sps_link), 'SPS LINK is not being displayed'
        path = Utils.click_link(self,sps_link, sps_link_url) 
        assert path == sps_link_url, 'SPS LINK is not working'

    @allure.title("Test SPS REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_sps_register_link
    def test_home_sps_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        sps_register_link = HomeLocator.getSpsRegisterLink(self)
        sps_register_link_url = self.CONST.get('SPS_REGISTER_LINK')
        assert Utils.is_displayed(self,sps_register_link), 'SPS REGISTER button is not being displayed'
        path = Utils.click_link(self,sps_register_link, sps_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == sps_register_link_url, 'SPS REGISTER Linkis not working'

    # PSMII
    @allure.title("Test PSMII  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_psmii_link
    def test_home_psmii_link(self, get_base_url):
        psmii_link = HomeLocator.getPsmiiLink(self)
        psmii_link_url = get_base_url + self.CONST.get('PSMII_LINK')
        assert Utils.is_displayed(self,psmii_link), 'PSMII LINK is not being displayed'
        path = Utils.click_link(self,psmii_link, psmii_link_url) 
        assert path == psmii_link_url, 'PSMII LINK is not working'

    @allure.title("Test PSMII REGISTER  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_psmii_register_link
    def test_home_psmii_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        psmii_register_link = HomeLocator.getPsmiiRegisterLink(self)
        psmii_register_link_url = self.CONST.get('PSMII_REGISTER_LINK')
        assert Utils.is_displayed(self,psmii_register_link), 'PSMII REGISTER button is not being displayed'
        path = Utils.click_link(self,psmii_register_link, psmii_register_link_url,True)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        assert path == psmii_register_link_url, 'PSMII REGISTER Link is not working'

    # EVIDENCE AGIL
    @allure.title("Test EVIDENCE AGIL  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_evidenceagil_link
    def test_home_evidenceagil_link(self, get_base_url):
        evidenceagil_link = HomeLocator.getEvidenceAgilLink(self)
        evidenceagil_link_url = get_base_url + self.CONST.get('EVIDENCE_AGIL_LINK')
        assert Utils.is_displayed(self,evidenceagil_link), 'EVIDENCEAGIL LINK  is not being displayed'
        path = Utils.click_link(self,evidenceagil_link, evidenceagil_link_url) 
        assert path == evidenceagil_link_url, 'EVIDENCEAGIL Link is not working'

    @allure.title("Test EVIDENCE AGIL REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and working")
    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.home_evidenceagil_register_link
    def test_home_evidenceagil_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        evidenceagil_register_link = HomeLocator.getEvidenceAgilRegisterLink(self)
        evidenceagil_register_link_url = self.CONST.get('EVIDENCE_AGIL_REGISTER_LINK')
        assert Utils.is_displayed(self,evidenceagil_register_link), 'EVIDENCEAGIL REGISTER button is not being displayed'
        path = Utils.click_link(self,evidenceagil_register_link, evidenceagil_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == evidenceagil_register_link_url, 'EVIDENCEAGIL REGISTER Link is not working'
