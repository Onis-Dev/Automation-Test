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
    CONTHEADER = CONSTANTS['HEADER']
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


    @allure.title("Test PSPO REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_pspo_register_link
    def test_home_pspo_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        pspo_register_link = HomeLocator.get_pspo_register_btn(self)
        pspo_register_link_url = self.CONST.get('PSPO_REGISTER_LINK')
        pspo_register_title = self.TITLES.get('PSPO_REGISTER_TITLE')
        assert Utils.is_displayed(self,pspo_register_link), 'PSPO REGISTER button is not being displayed'
        path = Utils.click_link(self,pspo_register_link, pspo_register_title, pspo_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == pspo_register_link_url, 'PSPO REGISTER Link is not working'


    @allure.title("Test PSM  link, redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psm_link
    def test_home_psm_link(self, get_base_url):
        psm_link = HomeLocator.get_psm_link(self)
        psm_link_url = get_base_url + self.CONST.get('PSM_LINK')
        psm_title = self.TITLES.get('PSM_TITLE')
        assert Utils.is_displayed(self,psm_link), 'PSM LINK  is not being displayed'
        path = Utils.click_link(self,psm_link, psm_title, psm_link_url) 
        assert path == psm_link_url, 'PSM LINK is not working'


    @allure.title("Test PSM REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_psm_register_link
    def test_home_psm_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        psm_register_link = HomeLocator.get_psm_register_btn(self)
        psm_register_link_url = self.CONST.get('PSM_REGISTER_LINK')
        psm_register_title = self.TITLES.get('PSM_REGISTER_TITLE')
        assert Utils.is_displayed(self,psm_register_link), 'PSM REGISTER button is not being displayed'
        path = Utils.click_link(self,psm_register_link, psm_register_title, psm_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == psm_register_link_url, 'PSM REGISTER Link is not working'


    @allure.title("Test SPS link redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_sps_link
    def test_home_sps_link(self, get_base_url):
        sps_link = HomeLocator.get_sps_link(self)
        sps_link_url = get_base_url + self.CONST.get('SPS_LINK')
        sps_title = self.TITLES.get('SPS_TITLE')
        assert Utils.is_displayed(self,sps_link), 'SPS LINK is not being displayed'
        path = Utils.click_link(self,sps_link, sps_title, sps_link_url) 
        assert path == sps_link_url, 'SPS LINK is not working'


    @allure.title("Test SPS REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_sps_register_link
    def test_home_sps_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        sps_register_link = HomeLocator.get_sps_register_btn(self)
        sps_register_link_url = self.CONST.get('SPS_REGISTER_LINK')
        sps_register_title = self.TITLES.get('SPS_REGISTER_TITLE')
        assert Utils.is_displayed(self,sps_register_link), 'SPS REGISTER button is not being displayed'
        path = Utils.click_link(self,sps_register_link, sps_register_title, sps_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == sps_register_link_url, 'SPS REGISTER Linkis not working'


    @allure.title("Test PSMII  button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psmii_link
    def test_home_psmii_link(self, get_base_url):
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
        evidenceagil_link = HomeLocator.get_evidence_agil_link(self)
        evidenceagil_link_url = get_base_url + self.CONST.get('EVIDENCE_AGIL_LINK')
        evidence_agil_title = self.TITLES.get('EVIDENCE_AGIL_TITLE')
        assert Utils.is_displayed(self,evidenceagil_link), 'EVIDENCEAGIL LINK  is not being displayed'
        path = Utils.click_link(self,evidenceagil_link, evidence_agil_title, evidenceagil_link_url) 
        assert path == evidenceagil_link_url, 'EVIDENCEAGIL Link is not working'


    @allure.title("Test EVIDENCE AGIL REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_evidenceagil_register_link
    def test_home_evidenceagil_register_link(self, get_base_url):
        self.driver.get(get_base_url)
        evidenceagil_register_link = HomeLocator.get_evidence_agil_register_btn(self)
        evidenceagil_register_link_url = self.CONST.get('EVIDENCE_AGIL_REGISTER_LINK')
        evidence_agil_register_title = self.TITLES.get('EVIDENCE_AGIL_REGISTER_TITLE')
        assert Utils.is_displayed(self,evidenceagil_register_link), 'EVIDENCEAGIL REGISTER button is not being displayed'
        path = Utils.click_link(self,evidenceagil_register_link, evidence_agil_register_title, evidenceagil_register_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == evidenceagil_register_link_url, 'EVIDENCEAGIL REGISTER Link is not working'


    #TRAINING CATALOGUE SECTION
    @allure.title("Test REQUEST CUSTOM TRAINING BUTTON redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_custom_training_btn
    def test_home_request_custom_training_btn(self, get_base_url):
        request_custom_training_btn = HomeLocator.get_request_custom_training_btn(self)
        request_custom_training_btn_url = get_base_url + self.CONST.get('CONTACTUS_REGISTER_BTN')
        contactus_register_title = self.TITLES.get('CONTACTUS_REGISTER_TITLE')
        assert Utils.is_displayed(self,request_custom_training_btn), 'REQUEST CUSTOM TRAINING BUTTON  is not being displayed'
        path = Utils.click_link(self,request_custom_training_btn, contactus_register_title, request_custom_training_btn_url) 
        assert path == request_custom_training_btn_url, 'REQUEST CUSTOM TRAINING LINK is not working'


    @allure.title("Test VIEW ALL UPCOMING TRAININGS BUTTON redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_view_all_upcoming_trainings_btn
    def test_home_view_all_upcoming_trainings_btn(self, get_base_url):
        self.driver.get(get_base_url)
        view_all_upcoming_trainings_btn = HomeLocator.get_view_all_upcoming_trainings_btn(self)
        view_all_upcoming_trainings_btn_url = get_base_url + self.CONST.get('VIEW_ALL_UPCOMING_TRAININGS_BTN')
        view_all_upcoming_trainings_title = self.TITLES.get('VIEW_ALL_UPCOMING_TRAININGS_TITLE')
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn), 'VIEW ALL UPCOMING TRAININGS BUTTON  is not being displayed'
        path = Utils.click_link(self,view_all_upcoming_trainings_btn, view_all_upcoming_trainings_title, view_all_upcoming_trainings_btn_url) 
        assert path == view_all_upcoming_trainings_btn_url, 'VIEW ALL UPCOMING TRAININGS LINK is not working'
        
        
    @allure.title("Test INTRO TO AGILE LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_intro_to_agile_link
    def test_home_intro_to_agile_link(self, get_base_url):
        self.driver.get(get_base_url)
        intro_to_agile_link = HomeLocator.get_intro_to_agile_link(self)
        intro_to_agile_link_url = get_base_url + self.CONST.get('INTRO_TO_AGILE_LINK')
        intro_to_agile_title = self.TITLES.get('INTRO_TO_AGILE_TITLE')
        assert Utils.is_displayed(self,intro_to_agile_link), 'INTRO TO AGILE LINK is not being displayed'
        path = Utils.click_link(self,intro_to_agile_link, intro_to_agile_title, intro_to_agile_link_url) 
        assert path == intro_to_agile_link_url, 'INTRO TO AGILE LINK is not working'
  
  
    @allure.title("Test INTRO TO AGILE REQUEST BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agil_btn
    def test_home_request_agil_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agil_btn = HomeLocator.get_request_agil_btn(self)       
        assert Utils.is_displayed(self,request_agil_btn), 'INTRO TO AGILE REQUEST BUTTON  is not being displayed'
   
   
    @allure.title("Test PROFESSIONAL SCRUM FOUNDATIONS LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psf_link
    def test_home_psf_link(self, get_base_url):
        psf_link = HomeLocator.get_psf_link(self)
        psf_link_url = get_base_url + self.CONST.get('PSF_LINK')
        psf_title = self.TITLES.get('PSF_TITLE')
        assert Utils.is_displayed(self,psf_link), 'PROFESSIONAL SCRUM FOUNDATIONS LINK is not being displayed'
        path = Utils.click_link(self,psf_link, psf_title, psf_link_url) 
        assert path == psf_link_url, 'PROFESSIONAL SCRUM FOUNDATIONS LINK is not working'
  
  
    @allure.title("Test PSF REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_psf_btn
    def test_home_request_psf_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_psf_btn = HomeLocator.get_request_psf_btn(self)       
        assert Utils.is_displayed(self,request_psf_btn), 'PSF REGISTER BUTTON  is not being displayed'
       
       
    @allure.title("Test PROFESSIONAL SCRUM DEVELOPER PSD LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psd_link
    def test_home_psd_link(self, get_base_url):
        psd_link = HomeLocator.get_psd_link(self)
        psd_link_url = get_base_url + self.CONST.get('PSD_LINK')
        psd_title = self.TITLES.get('PSD_TITLE')
        assert Utils.is_displayed(self,psd_link), 'PROFESSIONAL SCRUM DEVELOPER PSD LINK is not being displayed'
        path = Utils.click_link(self,psd_link, psd_title, psd_link_url) 
        assert path == psd_link_url, 'PROFESSIONAL SCRUM DEVELOPER PSD LINK is not working'

        
    @allure.title("Test PSD REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_psd_btn
    def test_home_request_psd_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_psd_btn = HomeLocator.get_request_psd_btn(self)       
        assert Utils.is_displayed(self,request_psd_btn), 'PSD REGISTER BUTTON  is not being displayed'


    @allure.title("Test PROFESSIONAL SCRUM MASTER PSM LINK redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_psm_link2
    def test_home_psm_link2(self, get_base_url):
        psm_link2 = HomeLocator.get_psm_link2(self)
        assert Utils.is_displayed(self,psm_link2), 'PROFESSIONAL SCRUM MASTER PSM LINK is not being displayed'
     
     
    @allure.title("Test PSM REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_psm_register_btn2
    def test_home_psm_register_btn2(self, get_base_url):
        psm_register_btn2 = HomeLocator.get_psm_register_btn2(self)
        assert Utils.is_displayed(self,psm_register_btn2), 'PSM REGISTER BUTTON is not being displayed'
     
     
    @allure.title("Test PSMII  button redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psmii_link2
    def test_home_psmii_link2(self, get_base_url):
        psmii_link2 = HomeLocator.get_psmii_link2(self)
        assert Utils.is_displayed(self,psmii_link2), 'PSMII LINK is not being displayed'

    @allure.title("Test PSMII REGISTER  button redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_psmii_register_btn2
    def test_home_psmii_register_btn2(self, get_base_url):
        psmii_register_btn2 = HomeLocator.get_psmii_register_btn2(self)
        assert Utils.is_displayed(self,psmii_register_btn2), 'PSMII REGISTER button is not being displayed'
        
    @allure.title("Test PSPO link redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_pspo_link2
    def test_home_pspo_link2(self, get_base_url):
        pspo_link2 = HomeLocator.get_pspo_link2(self)
        assert Utils.is_displayed(self,pspo_link2), 'PSPO LINK is not being displayed'

    @allure.title("Test PSPO REGISTER button redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_pspo_register_btn2
    def test_home_pspo_register_btn2(self, get_base_url):
        pspo_register_btn2 = HomeLocator.get_pspo_register_btn2(self)
        assert Utils.is_displayed(self,pspo_register_btn2), 'PSPO REGISTER button is not being displayed'
        

    @allure.title("Test SPS link redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_sps_link2
    def test_home_sps_link2(self, get_base_url):
        sps_link2 = HomeLocator.get_sps_link2(self)
        assert Utils.is_displayed(self,sps_link2), 'SPS LINK is not being displayed'


    @allure.title("Test SPS REGISTER button redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_sps_register_btn2
    def test_home_sps_register_btn2(self, get_base_url):
        sps_register_btn2 = HomeLocator.get_sps_register_btn2(self)
        assert Utils.is_displayed(self,sps_register_btn2), 'SPS REGISTER button is not being displayed'
    
    
    @allure.title("Test PROFESSIONAL AGIL LEADERSHIP ESSENTIALS LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_pal_e_link
    def test_home_pal_e_link(self, get_base_url):
        pal_e_link = HomeLocator.get_pal_e_link(self)
        pal_e_link_url = get_base_url + self.CONST.get('PAL_E_LINK')
        pal_e_title = self.TITLES.get('PAL_E_TITLE')
        assert Utils.is_displayed(self,pal_e_link), 'PROFESSIONAL AGIL LEADERSHIP ESSENTIALS link is not being displayed'
        path = Utils.click_link(self,pal_e_link, pal_e_title, pal_e_link_url) 
        assert path == pal_e_link_url, 'PROFESSIONAL AGIL LEADERSHIP ESSENTIALS LINK is not working'
         
         
    @allure.title("Test PALE REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_pal_e_btn
    def test_home_request_pal_e_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_pal_e_btn = HomeLocator.get_request_pal_e_btn(self)       
        assert Utils.is_displayed(self,request_pal_e_btn), 'PALE REGISTER BUTTON  is not being displayed'
        
        
    @allure.title("Test EVIDENCE AGIL  LINK redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_evidence_base_agility_link2
    def test_home_evidence_base_agility_link2(self, get_base_url):
        evidence_base_agility_link2 = HomeLocator.get_evidence_agil_link(self)
        assert Utils.is_displayed(self,evidence_base_agility_link2), 'EVIDENCEAGIL LINK  is not being displayed'


    @allure.title("Test EVIDENCE AGIL REGISTER button redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_evidence_base_agility_register_btn2
    def test_home_evidence_base_agility_register_btn2(self, get_base_url):
        evidence_base_agility_register_btn2 = HomeLocator.get_evidence_agil_register_btn(self)
        assert Utils.is_displayed(self,evidence_base_agility_register_btn2), 'EVIDENCEAGIL REGISTER button is not being displayed'
     
     
    @allure.title("Test KANBA SYSTEM DESIGN LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_kanba_system_design_link
    def test_home_kanba_system_design_link(self, get_base_url):
        kanba_system_design_link = HomeLocator.get_kanba_system_design_link(self)
        kanba_system_design_link_url = get_base_url + self.CONST.get('KANBA_SYSTEM_DESIGN_LINK')
        kanba_system_design_title = self.TITLES.get('KANBA_SYSTEM_DESIGN_TITLE')
        assert Utils.is_displayed(self,kanba_system_design_link), 'KANBA SYSTEM DESIGN LINK is not being displayed'
        path = Utils.click_link(self,kanba_system_design_link, kanba_system_design_title, kanba_system_design_link_url) 
        assert path == kanba_system_design_link_url, 'KANBA SYSTEM DESIGN LINK is not working'
        
        
    @allure.title("Test KANBA SYSTEM DESIGN REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_kanba_s_btn
    def test_home_request_kanba_s_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_kanba_s_btn = HomeLocator.get_request_kanba_s_btn(self)       
        assert Utils.is_displayed(self,request_kanba_s_btn), 'KANBA SYSTEM DESIGN REGISTER BUTTON  is not being displayed'
       

    @allure.title("Test KANBA MANAGEMENT PROFESSIONAL LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_kanba_management_prof_link
    def test_home_kanba_management_prof_link(self, get_base_url):
        kanba_management_prof_link = HomeLocator.get_kanba_management_prof_link(self)
        kanba_management_prof_link_url = get_base_url + self.CONST.get('KANBA_MANAGEMENT_PROF_LINK')
        kanba_management_prof_title = self.TITLES.get('KANBA_MANAGEMENT_PROF_TITLE')
        assert Utils.is_displayed(self,kanba_management_prof_link), 'KANBA MANAGEMENT PROFESSIONAL LINK is not being displayed'
        path = Utils.click_link(self,kanba_management_prof_link, kanba_management_prof_title, kanba_management_prof_link_url) 
        assert path == kanba_management_prof_link_url, 'KANBA MANAGEMENT PROFESSIONAL LINK is not working'
        
        
    @allure.title("Test KANBA MANAGEMENT PROFESSIONAL REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_kanba_m_btn
    def test_home_request_kanba_m_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_kanba_m_btn = HomeLocator.get_request_kanba_m_btn(self)       
        assert Utils.is_displayed(self,request_kanba_m_btn), 'KANBA MANAGEMENT PROFESSIONAL REGISTER BUTTON  is not being displayed'
       

    @allure.title("Test TEAM KANBAN PRACTITIONER LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_team_kanban_practitioner_link
    def test_home_team_kanban_practitioner_link(self, get_base_url):
        team_kanban_practitioner_link = HomeLocator.get_team_kanban_practitioner_link(self)
        team_kanban_practitioner_link_url = get_base_url + self.CONST.get('TEAM_KANBAN_PRACTITIONER_LINK')
        team_kanban_practitioner_title = self.TITLES.get('TEAM_KANBAN_PRACTITIONER_TITLE')
        assert Utils.is_displayed(self,team_kanban_practitioner_link), 'TEAM KANBAN PRACTITIONER LINK is not being displayed'
        path = Utils.click_link(self,team_kanban_practitioner_link, team_kanban_practitioner_title, team_kanban_practitioner_link_url) 
        assert path == team_kanban_practitioner_link_url, 'TEAM KANBAN PRACTITIONER LINK is not working'
        
        
    @allure.title("Test TEAM KANBAN PRACTITIONER REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_kanba_p_btn
    def test_home_request_kanba_p_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_kanba_p_btn = HomeLocator.get_request_kanba_p_btn(self)       
        assert Utils.is_displayed(self,request_kanba_p_btn), 'TEAM KANBAN PRACTITIONER REGISTER BUTTON  is not being displayed'
       
       
    @allure.title("Test PSK LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psk_link
    def test_home_psk_link(self, get_base_url):
        psk_link = HomeLocator.get_psk_link(self)
        psk_link_url = get_base_url + self.CONST.get('PSK_LINK')
        psk_title = self.TITLES.get('PSK_TITLE')
        assert Utils.is_displayed(self,psk_link), 'PSK LINK is not being displayed'
        path = Utils.click_link(self,psk_link, psk_title, psk_link_url) 
        assert path == psk_link_url, 'PSK LINK is not working'
        
        
    @allure.title("Test PSK REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_psk_btn
    def test_home_request_psk_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_psk_btn = HomeLocator.get_request_psk_btn(self)       
        assert Utils.is_displayed(self,request_psk_btn), 'PSK REGISTER BUTTON  is not being displayed'
       
       
    @allure.title("Test MANAGEMENT3 0 LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_m3_0_link
    def test_home_m3_0_link(self, get_base_url):
        m3_0_link = HomeLocator.get_m3_0_link(self)
        m3_0_link_url = get_base_url + self.CONST.get('M3_0_LINK')
        m3_0_title = self.TITLES.get('M3_0_TITLE')
        assert Utils.is_displayed(self,m3_0_link), 'MANAGEMENT3 0 LINK is not being displayed'
        path = Utils.click_link(self,m3_0_link, m3_0_title, m3_0_link_url) 
        assert path == m3_0_link_url, 'MANAGEMENT3 0 LINK is not working'
        
        
    @allure.title("Test MANAGEMENT3 0 REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_m30_btn
    def test_home_request_m30_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_m30_btn = HomeLocator.get_request_m30_btn(self)       
        assert Utils.is_displayed(self,request_m30_btn), 'MANAGEMENT3 0 REGISTER BUTTON  is not being displayed'


    @allure.title("Test PROFESSIONAL SCRUM WITH USER EXPERIENCE LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_psu_link
    def test_home_psu_link(self, get_base_url):
        psu_link = HomeLocator.get_psu_link(self)
        psu_link_url = get_base_url + self.CONST.get('PSU_LINK')
        psu_title = self.TITLES.get('PSU_TITLE')
        assert Utils.is_displayed(self,psu_link), 'PROFESSIONAL SCRUM WITH USER EXPERIENCE LINK is not being displayed'
        path = Utils.click_link(self,psu_link, psu_title, psu_link_url) 
        assert path == psu_link_url, 'PROFESSIONAL SCRUM WITH USER EXPERIENCE LINK is not working'
        
        
    @allure.title("Test PSU REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_psu_btn
    def test_home_request_psu_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_psu_btn = HomeLocator.get_request_psu_btn(self)       
        assert Utils.is_displayed(self,request_psu_btn), 'PSU REGISTER BUTTON  is not being displayed'
       
    #AGILE PRACTICES AND TOOLS
       
    @allure.title("Test AGILE PRACTICES AND TOOLS LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test BEHAVIOR DRIVEN DEVELOPMENT LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test BDD REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_bdd_btn
    def test_home_request_bdd_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_bdd_btn = HomeLocator.get_request_bdd_btn(self)   
        assert Utils.is_displayed(self,request_bdd_btn), 'BDD REGISTER BUTTON  is not being displayed'


    @allure.title("Test AGILE TESTING WORKSHOP LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE TESTING WORKSHOP REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agiltesting_btn
    def test_home_request_agiltesting_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agiltesting_btn = HomeLocator.get_request_agiltesting_btn(self)  
        assert Utils.is_displayed(self,request_agiltesting_btn), 'AGILE TESTING WORKSHOP REGISTER is not being displayed'
       
    #AGILE CULTURE
       
    @allure.title("Test AGILE CULTURE LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE DIVERSITY LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE DIVERSITY REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agildiverity_btn
    def test_home_request_agildiverity_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agildiverity_btn = HomeLocator.get_request_agildiverity_btn(self)  
        assert Utils.is_displayed(self,request_agildiverity_btn), 'AGILE DIVERSITY REGISTER is not being displayed'
       
       
    @allure.title("Test AGILE CONFLICT LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE CONFLICT REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agilconflict_btn
    def test_home_request_agilconflict_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilconflict_btn = HomeLocator.get_request_agilconflict_btn(self)  
        assert Utils.is_displayed(self,request_agilconflict_btn), 'AGILE CONFLICT REGISTER is not being displayed'
        
        
    @allure.title("Test AGILE MOTIVATION LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE MOTIVATION REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agilmotivation_btn
    def test_home_request_agilmotivation_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilmotivation_btn = HomeLocator.get_request_agilmotivation_btn(self)  
        assert Utils.is_displayed(self,request_agilmotivation_btn), 'AGILE MOTIVATION REGISTER BUTTON is not being displayed'
        
        
    @allure.title("Test AGILE CHANGE LINK redirect is displayed and working") 
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
        
        
    @allure.title("Test AGILE CHANGE REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_agilchanges_btn
    def test_home_request_agilchanges_btn(self, get_base_url):
        self.driver.get(get_base_url)
        request_agilchanges_btn = HomeLocator.get_request_agilchanges_btn(self)  
        assert Utils.is_displayed(self,request_agilchanges_btn), 'AGILE CHANGE REGISTER BUTTON is not being displayed'
       
    #CUSTOM TRAINING
       
    @allure.title("Test CUSTOM TRAINING LINK redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_ct_btn
    def test_home_request_ct_btn(self, get_base_url):
        request_ct_btn = HomeLocator.get_request_ct_btn(self)  
        assert Utils.is_displayed(self,request_ct_btn), 'CUSTOM TRAINING LINK is not being displayed'


    @allure.title("Test RESQUEST CUSTOM TRAINING BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_req_ct_btn
    def test_home_request_req_ct_btn(self, get_base_url):
        request_req_ct_btn = HomeLocator.get_request_req_ct_btn(self)  
        assert Utils.is_displayed(self,request_req_ct_btn), 'RESQUEST CUSTOM TRAINING BUTTON is not being displayed'

    #AGILE EVENTS

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

    @allure.title("Test SCRUM PULSE WEBINAR LINK redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_scrum_pulse_webinar_link
    def test_home_scrum_pulse_webinar_link(self, get_base_url):
        self.driver.get(get_base_url)
        scrum_pulse_webinar_link = HomeLocator.get_scrum_pulse_webinar_link(self)
        scrum_pulse_webinar_link_url = self.CONST.get('SCRUM_PULSE_WEBINAR_LINK')
        scrum_pulse_webinar_title = self.TITLES.get('SCRUM_PULSE_WEBINAR_TITLE')
        assert Utils.is_displayed(self,scrum_pulse_webinar_link), 'SCRUM PULSE WEBINAR LINK is not being displayed'
        path = Utils.click_link(self,scrum_pulse_webinar_link, scrum_pulse_webinar_title, scrum_pulse_webinar_link_url,True) 
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert path == scrum_pulse_webinar_link_url, 'SCRUM PULSE WEBINAR Link is not working'
        
        
    @allure.title("Test SCRUM PULSE WEBINAR REGISTER BUTTON redirect is displayed") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_scrum_pulse_webinar_btn
    def test_home_scrum_pulse_webinar_link2(self, get_base_url):
        self.driver.get(get_base_url)
        scrum_pulse_webinar_link2 = HomeLocator.get_scrum_pulse_webinar_link2(self)
        assert Utils.is_displayed(self,scrum_pulse_webinar_link2), 'SCRUM PULSE WEBINAR REGISTER BUTTON is not being displayed'

    
    @allure.title("Test AGILE GALLERY SLIDER  button is displayed and working") 
    @allure.description(" Test if AGILE GALLERY slider is working correctly")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_gallery_slider
    def test_home_agile_gallery_slider(self, get_base_url):
        slider = HomeLocator.get_agile_gallery_slider(self)
        assert Utils.is_displayed(self, slider), "slider content is not being displayed"
        slider_titles = HomeLocator.get_agile_gallery_slider_texts(self)
        sliderControl = HomeLocator.get_agile_gallery_controllers(self)
        page_count = 0
        has_text = True
        while page_count < len(sliderControl):
            sliderControl[page_count].click()
            print(slider_titles[page_count].get_attribute('text'), "TEXTSSSS")
            if slider_titles[page_count].get_attribute('text') == None or slider_titles[page_count].get_attribute('text') == "":
                has_text = False
                break
            page_count += 1
        assert has_text, "AGILE GALLERY SLIDER is not working correctly"

    @allure.title("Test AGILE BLOG SLIDER  button is displayed and working") 
    @allure.description(" Test if AGILE BLOG slider is working correctly")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_blog_slider
    def test_home_agile_blog_slider(self, get_base_url):
        slider = HomeLocator.get_agile_blog_slider(self)
        assert Utils.is_displayed(self, slider), "slider content is not being displayed"
        slider_titles = HomeLocator.get_agile_blog_slider_texts(self)
        sliderControl = HomeLocator.get_agile_blog_controllers(self)
        page_count = 0
        has_text = True
        while page_count < len(sliderControl):
            sliderControl[page_count].click()
            if slider_titles[page_count].get_attribute('textContent') == None or slider_titles[page_count].get_attribute('textContent') == "":
                has_text = False
                break
            page_count += 1
        assert has_text, "AGILE BLOG SLIDER is not working correctly"


    @allure.title("Test AGILE VIDEOS IMAGE LINK is displayed and working") 
    @allure.description(" Test if AGILE VIDEOS IMAGE LINK is working correctly")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_agile_videos_image_link
    def test_home_agile_videos_image_link(self, get_base_url):
        image_link = HomeLocator.get_agile_videos_image_link(self)
        image_link_url = get_base_url + self.CONTHEADER.get('SUBMENU_AGILE_VIDEOS')
        assert Utils.is_displayed(self,image_link), "AGILE VIDEOS IMAGE is not being displayed"
        path = Utils.click_link(self,image_link, self.TITLES.get('RESOURCES_AGILE_VIDEOS_TITLE'), image_link_url) 
        assert path == image_link_url, 'AGILE VIDEOS IMAGE LINK is not working'

    @allure.title("Test AGILE PRESENTATIONS IMAGE LINK is displayed and working") 
    @allure.description(" Test if AGILE PRESENTATIONS IMAGE LINK is working correctly")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_agile_presentations_image_link
    def test_home_agile_presentations_image_link(self, get_base_url):
        image_link = HomeLocator.get_agile_presentations_image_link(self)
        image_link_url = get_base_url + self.CONTHEADER.get('SUBMENU_AGILE_PRESENTATIONS')
        assert Utils.is_displayed(self,image_link), "AGILE PRESENTATIONS IMAGE is not being displayed"
        path = Utils.click_link(self,image_link, self.TITLES.get('RESOURCES_AGILE_PRESENTATIONS_TITLE'), image_link_url) 
        assert path == image_link_url, 'AGILE PRESENTATIONS IMAGE LINK is not working'