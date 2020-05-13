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
class TestTrainingCatalogue:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']

    @allure.title("Test REQUEST CUSTOM TRAINING BUTTON redirect is displayed and working") 
    @allure.description(" Test if link is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_request_custom_training_btn
    def test_home_request_custom_training_btn(self, get_base_url):
        self.driver.get(get_base_url)
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