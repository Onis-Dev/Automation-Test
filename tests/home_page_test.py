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
    TITLES = CONSTANTS['TITLES_PAGES']
    
   #LEARN MORE
    @allure.title("Test Learn More button redirect is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_learn_more_button
    def test_learn_more_redirect(self, get_base_url):
        learn_more_btn = HomeLocator.get_learn_more_btn(self)
        learn_more_url = get_base_url + self.CONST.get('LEARN_MORE_REDIRECT')
        learn_more_title = self.TITLES.get('LEARN_MORE_TITLE')
        assert Utils.is_displayed(self,learn_more_btn), 'Learn More button is no being displayed'
        path = Utils.click_link(self,learn_more_btn, learn_more_title, learn_more_url) 
        assert path == learn_more_url, 'LEARN MORE REDIRECT is not working'
    
    #UPCOMING TRAININGS

    @allure.title("Test PSPO link redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_pspo_link
    def test_home_pspo_link(self, get_base_url):
        self.driver.get(get_base_url)
        pspo_link = HomeLocator.get_pspo_link(self)
        pspo_link_url = get_base_url + self.CONST.get('PSPO_LINK')
        pspo_title = self.TITLES.get('PSPO_TITLE')
        assert Utils.is_displayed(self,pspo_link), 'PSPO LINK is not being displayed'
        path = Utils.click_link(self,pspo_link, pspo_title, pspo_link_url) 
        assert path == pspo_link_url, 'PSPO_LINK is not working'


    # @allure.title("Test PSPO REGISTER button redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_pspo_register_link
    # def test_home_pspo_register_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     pspo_register_link = HomeLocator.get_pspo_register_btn(self)
    #     pspo_register_link_url = self.CONST.get('PSPO_REGISTER_LINK')
    #     pspo_register_title = self.TITLES.get('PSPO_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,pspo_register_link), 'PSPO REGISTER button is not being displayed'
    #     path = Utils.click_link(self,pspo_register_link, pspo_register_title, pspo_register_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == pspo_register_link_url, 'PSPO REGISTER Link is not working'


    @allure.title("Test PSM  link, redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psm_link
    def test_home_psm_link(self, get_base_url):
        self.driver.get(get_base_url)
        psm_link = HomeLocator.get_psm_link(self)
        psm_link_url = get_base_url + self.CONST.get('PSM_LINK')
        psm_title = self.TITLES.get('PSM_TITLE')
        assert Utils.is_displayed(self,psm_link), 'PSM LINK  is not being displayed'
        path = Utils.click_link(self,psm_link, psm_title, psm_link_url) 
        assert path == psm_link_url, 'PSM LINK is not working'


    # @allure.title("Test PSM REGISTER button redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_psm_register_link
    # def test_home_psm_register_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     psm_register_link = HomeLocator.get_psm_register_btn(self)
    #     psm_register_link_url = self.CONST.get('PSM_REGISTER_LINK')
    #     psm_register_title = self.TITLES.get('PSM_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,psm_register_link), 'PSM REGISTER button is not being displayed'
    #     path = Utils.click_link(self,psm_register_link, psm_register_title, psm_register_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == psm_register_link_url, 'PSM REGISTER Link is not working'


    @allure.title("Test SPS link redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_sps_link
    def test_home_sps_link(self, get_base_url):
        self.driver.get(get_base_url)
        sps_link = HomeLocator.get_sps_link(self)
        sps_link_url = get_base_url + self.CONST.get('SPS_LINK')
        sps_title = self.TITLES.get('SPS_TITLE')
        assert Utils.is_displayed(self,sps_link), 'SPS LINK is not being displayed'
        path = Utils.click_link(self,sps_link, sps_title, sps_link_url) 
        assert path == sps_link_url, 'SPS LINK is not working'


    # @allure.title("Test SPS REGISTER button redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_sps_register_link
    # def test_home_sps_register_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     sps_register_link = HomeLocator.get_sps_register_btn(self)
    #     sps_register_link_url = self.CONST.get('SPS_REGISTER_LINK')
    #     sps_register_title = self.TITLES.get('SPS_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,sps_register_link), 'SPS REGISTER button is not being displayed'
    #     path = Utils.click_link(self,sps_register_link, sps_register_title, sps_register_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == sps_register_link_url, 'SPS REGISTER Linkis not working'


    @allure.title("Test PSMII  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psmii_link
    def test_home_psmii_link(self, get_base_url):
        self.driver.get(get_base_url)
        psmii_link = HomeLocator.get_psmii_link(self)
        psmii_link_url = get_base_url + self.CONST.get('PSMII_LINK')
        psmii_title = self.TITLES.get('PSMII_TITLE')
        assert Utils.is_displayed(self,psmii_link), 'PSMII LINK is not being displayed'
        path = Utils.click_link(self,psmii_link, psmii_title, psmii_link_url) 
        assert path == psmii_link_url, 'PSMII LINK is not working'


    # @allure.title("Test PSMII REGISTER  button redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_psmii_register_link
    # def test_home_psmii_register_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     psmii_register_link = HomeLocator.get_psmii_register_btn(self)
    #     psmii_register_link_url = self.CONST.get('PSMII_REGISTER_LINK')
    #     psmii_register_title = self.TITLES.get('PSMII_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,psmii_register_link), 'PSMII REGISTER button is not being displayed'
    #     path = Utils.click_link(self,psmii_register_link, psmii_register_title, psmii_register_link_url,True)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0]) 
    #     assert path == psmii_register_link_url, 'PSMII REGISTER Link is not working'


    @allure.title("Test EVIDENCE AGIL  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_evidenceagil_link
    def test_home_evidenceagil_link(self, get_base_url):
        self.driver.get(get_base_url)
        evidenceagil_link = HomeLocator.get_evidence_agil_link(self)
        evidenceagil_link_url = get_base_url + self.CONST.get('EVIDENCE_AGIL_LINK')
        evidence_agil_title = self.TITLES.get('EVIDENCE_AGIL_TITLE')
        assert Utils.is_displayed(self,evidenceagil_link), 'EVIDENCEAGIL LINK  is not being displayed'
        path = Utils.click_link(self,evidenceagil_link, evidence_agil_title, evidenceagil_link_url) 
        assert path == evidenceagil_link_url, 'EVIDENCEAGIL Link is not working'


    # @allure.title("Test EVIDENCE AGIL REGISTER button redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_evidenceagil_register_link
    # def test_home_evidenceagil_register_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     evidenceagil_register_link = HomeLocator.get_evidence_agil_register_btn(self)
    #     evidenceagil_register_link_url = self.CONST.get('EVIDENCE_AGIL_REGISTER_LINK')
    #     evidence_agil_register_title = self.TITLES.get('EVIDENCE_AGIL_REGISTER_TITLE')
    #     assert Utils.is_displayed(self,evidenceagil_register_link), 'EVIDENCEAGIL REGISTER button is not being displayed'
    #     path = Utils.click_link(self,evidenceagil_register_link, evidence_agil_register_title, evidenceagil_register_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == agile_devops_meetup_register_btn_url, 'AGILE DEVOPS MEETUP REGISTER Link is not working'
    #     assert path == evidenceagil_register_link_url, 'EVIDENCEAGIL REGISTER Link is not working'

