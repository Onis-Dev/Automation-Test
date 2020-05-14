import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

"""Class to get all elements from HOME section"""
class HomeLocator:
    # Learn More
    """Get learn more button"""
    def get_learn_more_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('LEARN_MORE_BTN_XPATH'))
    #*****UPCOMING TRAININGS
    # PSPO
    """Get PSPO link element"""
    def get_pspo_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSPO_LINK_XPATH'))

    """Get PSPO button register element"""
    def get_pspo_register_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSPO_REGISTER_BTN_XPATH'))

    # PSM
    """Get PSM link element"""
    def get_psm_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSM_LINK_XPATH'))

    """Get PSM button register element"""
    def get_psm_register_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSM_REGISTER_BTN_XPATH'))

    # SPS
    """Get SPS link element"""
    def get_sps_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('SPS_LINK_XPATH'))

    """Get SPS button register element"""
    def get_sps_register_btn(self):
        return Utils.find_element_by_xpath(self,  self.ELEMENTS.get('SPS_REGISTER_BTN_XPATH'))

    # PSMII
    """Get PSMII link element"""
    def get_psmii_link(self):
        return Utils.find_element_by_xpath(self,self.ELEMENTS.get('PSMII_LINK_XPATH'))

    """Get PSMII button register element"""
    def get_psmii_register_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSMII_REGISTER_BTN_XPATH'))

    # EVIDENCE AGIL
    """Get EVIDENCE AGIL link element"""
    def get_evidence_agil_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('EVIDENCE_AGILE_LINK_XPATH'))

    """Get EVIDENCE AGIL button register element"""
    def get_evidence_agil_register_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('EVIDENCE_AGILE_REGISTER_BTN_XPATH'))

    ##
    """Get CONTACTUS button register element"""
    def get_request_custom_training_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_CUSTOM_TRAINING_BTN_XPATH'))

    """Get VIEW ALL UPCOMING TRAININGS BTN"""
    def get_view_all_upcoming_trainings_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('UPCOMING_TRAINING_BTN_XPATH'))

    """Get INTRO TO AGILE link element"""
    def get_intro_to_agile_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('INTRO_TO_AGILE_LINK_XPATH'))

    """Get CONTACTUS button2 register element"""
    def get_request_agil_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILE_BTN_XPATH'))

    """Get PSF link element"""
    def get_psf_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSF_LINK_XPATH'))

    """Get CONTACTUS button3 register element"""
    def get_request_psf_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSF_REQUEST_BTN_XPATH'))

    """Get PSD link element"""
    def get_psd_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSD_LINK_XPATH'))

    """Get CONTACTUS button4 register element"""
    def get_request_psd_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSD_REQUEST_BTN_XPATH'))

    """Get PSM link2 element"""
    def get_psm_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSM_LINK2_XPATH'))

    """Get PSM button2 register element"""
    def get_psm_register_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSM_REGISTER_BTN2_XPATH'))

    """Get PSMII link2 element"""
    def get_psmii_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSMII_LINK2_XPATH'))

    """Get PSMII button2 register element"""
    def get_psmii_register_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSMII_REGISTER_BTN2_XPATH'))

    """Get PSPO link2 element"""
    def get_pspo_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSPO_LINK2_XPATH'))

    """Get PSPO button2 register element"""
    def get_pspo_register_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSPO_REGISTER_BTN2_XPATH'))

    """Get SPS link2 element"""
    def get_sps_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('SPS_LINK2_XPATH'))

    """Get SPS button2 register element"""
    def get_sps_register_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('SPS_REGISTER_BTN2_XPATH'))

    """Get PAL E link element"""
    def get_pal_e_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PAL_E_LINK_XPATH'))

    """Get CONTACTUS button5 register element"""
    def get_request_pal_e_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_PAL_E_BTN_XPATH'))

    """Get EVIDENCE BASE AGILITY link2 element"""
    def get_evidence_base_agility_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('EVIDENCE_BASE_AGILITY_LINK2_XPATH'))

    """Get EVIDENCE BASE AGILITY button2 register element"""
    def get_evidence_base_agility_register_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('EVIDENCE_BASE_AGILITY_REGISTER_BTN2_XPATH'))

    """Get KANBA SYSTEM DESIGN link element"""
    def get_kanba_system_design_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('KANBA_SYSTEM_DESIGN_LINK_XPATH'))

    """Get CONTACTUS button6 register element"""
    def get_request_kanba_s_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_KANBA_S_BTN_XPATH'))

    """Get KANBA MANAGEMENT PROF link element"""
    def get_kanba_management_prof_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('KANBA_MANAGEMENT_PROF_LINK_XPATH'))

    """Get CONTACTUS button7 register element"""
    def get_request_kanba_m_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_KANBA_M_BTN_XPATH'))

    """Get TEAM KANBAN PRACTITIONER link element"""
    def get_team_kanban_practitioner_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('TEAM_KANBAN_PRACTITIONER_LINK_XPATH'))

    """Get CONTACTUS button8 register element"""
    def get_request_kanba_p_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_KANBA_P_BTN_XPATH'))

    """Get PSK link element"""
    def get_psk_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSK_LINK_XPATH'))

    """Get CONTACTUS button9 register element"""
    def get_request_psk_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_PSK_BTN_XPATH'))

    """Get M3 0 link element"""
    def get_m3_0_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('M3_0_LINK_XPATH'))

    """Get CONTACTUS button10 register element"""
    def get_request_m30_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_M30_BTN_XPATH'))

    """Get PSU link element"""
    def get_psu_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('PSU_LINK_XPATH'))

    """Get CONTACTUS button11 register element"""
    def get_request_psu_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_PSU_BTN_XPATH'))

    """Get AGILE PRACTICES AND TOOLS link element"""
    def get_agile_practices_and_tools_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_PRACTICES_AND_TOOLS_LINK_XPATH'))

    """Get BDD link element"""
    def get_bdd_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('BDD_LINK_XPATH'))

    """Get CONTACTUS button12 register element"""
    def get_request_bdd_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_BDD_BTN_XPATH'))

    """Get AGILE TESTING WORKSHOP link element"""
    def get_agile_testing_workshop_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_TESTING_WORKSHOP_LINK_XPATH'))

    """Get CONTACTUS button13 register element"""
    def get_request_agiltesting_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILTESTING_BTN_XPATH'))

    """Get AGILE CULTURE link element"""
    def get_agile_culture_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_CULTURE_LINK_XPATH'))

    """Get AGILE DIVERSITY link element"""
    def get_agile_diversity_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_DIVERSITY_LINK_XPATH'))

    """Get CONTACTUS button14 register element"""
    def get_request_agildiverity_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILDIVERITY_BTN_XPATH'))

    """Get AGILE CONFLICT link element"""
    def get_agile_conflict_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_CONFLICT_LINK_XPATH'))

    """Get CONTACTUS button15 register element"""
    def get_request_agilconflict_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILCONFLICT_BTN_XPATH'))

    """Get AGILE MOTIVATION link element"""
    def get_agile_motivation_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_MOTIVATION_LINK_XPATH'))

    """Get CONTACTUS button16 register element"""
    def get_request_agilmotivation_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILMOTIVATION_BTN_XPATH'))

    """Get AGILE CHANGE link element"""
    def get_agile_change_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_CHANGE_LINK_XPATH'))

    """Get CONTACTUS button17 register element"""
    def get_request_agilchanges_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_AGILCHANGES_BTN_XPATH'))

    """Get CONTACTUS button18 register element"""
    def get_request_ct_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_CT_BTN_XPATH'))

    """Get CONTACTUS button19 register element"""
    def get_request_req_ct_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_REQ_CT_BTN_XPATH'))

    """Get VIEW ALL UPCOMING TRAININGS BTN2"""		
    def get_view_all_upcoming_trainings_btn2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('VIEW_ALL_UPCOMING_TRAININGS_BTN2_XPATH'))

    """Get CONTACTUS button20 register element"""
    def get_request_uncoming_t_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('REQUEST_UNCOMING_T_BTN_XPATH'))

    """Get VIEW ALL UPCOMING TRAININGS BTN3"""		
    def get_view_all_upcoming_trainings_btn3(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('VIEW_ALL_UPCOMING_TRAININGS_BTN3_XPATH'))

    """Get SCCRUM PULSE WEBINAR link element"""
    def get_scrum_pulse_webinar_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('SCRUM_PULSE_WEBINAR_LINK_XPATH'))

    """Get SCRUM PULSE WEBINAR link2 element"""		
    def get_scrum_pulse_webinar_link2(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('SCRUM_PULSE_WEBINAR_LINK2_XPATH'))
    
    """Get agile gallery slider element"""
    def get_agile_gallery_slider(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_GALLERY_SLIDER_XPATH'))

    """Get agile gallery slider titles"""
    def get_agile_gallery_slider_texts(self):
        return Utils.find_elements_by_css_selector(self, self.ELEMENTS.get('AGILE_GALLERY_SLIDER_TEXTS_XPATH'), self.ELEMENTS.get('AGILE_GALLERY_SLIDER_TEXTS_CSS_SELECTOR'))

    """Get agile gallery slider controls"""
    def get_agile_gallery_controllers(self):
        return Utils.find_elements_by_tag_name(self, self.ELEMENTS.get('AGILE_GALLERY_CONTROLLERS_XPATH'), self.ELEMENTS.get('AGILE_GALLERY_CONTROLLERS_TAG_NAME'))
    
    """Get agile blog slider element"""
    def get_agile_blog_slider(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_BLOG_SLIDER_XPATH'))

    """Get agile blog slider titles"""
    def get_agile_blog_slider_texts(self):
        return Utils.find_elements_by_tag_name(self,self.ELEMENTS.get('AGILE_BLOG_SLIDER_TEXTS_XPATH'), self.ELEMENTS.get('AGILE_BLOG_SLIDER_TEXTS_TAG_NAME'))

    """Get agile blog slider controls"""
    def get_agile_blog_controllers(self):
        return Utils.find_elements_by_tag_name(self,self.ELEMENTS.get('AGILE_BLOG_CONTROLLERS_XPATH'), self.ELEMENTS.get('AGILE_BLOG_CONTROLLERS_TAG_NAME'))

    """Get agile videos image link element"""
    def get_agile_videos_image_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_VIDEOS_IMAGE_LINK_XPATH'))
    
    """Get agile presentations image link element"""
    def get_agile_presentations_image_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_PRESENTATIONS_IMAGE_LINK_XPATH'))

    #AGILE PARTNERS
    """Get AGILE PARTNERS link element"""		
    def get_agile_partners_link(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AGILE_PARTNERS_LINK_XPATH'))

    """Get READ MORE RAVI VERMA element"""		
    def get_read_more_ravi_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_RAVI_BTN_XPATH'))

    """Get READ MORE MARK NONEMAN element"""		
    def get_read_more_mark_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_MARK_BTN_XPATH'))
        
    """Get READ MORE CHARLES BRADLEY element"""		
    def get_read_more_charles_b_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_CHARLES_B_BTN_XPATH'))

    """Get READ MORE CHARLES SUSCHECK element"""		
    def get_read_more_charles_s_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_CHARLES_S_BTN_XPATH'))

    """Get READ MORE HIREN element"""		
    def get_read_more_hiren_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_HIREN_BTN_XPATH'))

    """Get READ MORE RICH VISOTCKY element"""		
    def get_read_more_rich_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_RICH_BTN_XPATH'))

    """Get READ MORE JULEE element"""		
    def get_read_more_julee_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_JULEE_BTN_XPATH'))

    """Get READ MORE MAGDALENA element"""		
    def get_read_more_magdalena_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_MAGDALENA_BTN_XPATH'))

    """Get READ MORE JILL element"""		
    def get_read_more_jill_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_JILL_BTN_XPATH'))

    """Get READ MORE NAGESH element"""		
    def get_read_more_nagesh_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('READ_MORE_NAGESH_BTN_XPATH'))
    