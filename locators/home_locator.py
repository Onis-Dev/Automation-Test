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
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[1]/div/div[2]/div[2]/a')
    #*****UPCOMING TRAININGS
    # PSPO
    """Get PSPO link element"""
    def get_pspo_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/a')

    """Get PSPO button register element"""
    def get_pspo_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[5]/a')

    # PSM
    """Get PSM link element"""
    def get_psm_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/a')

    """Get PSM button register element"""
    def get_psm_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/a')

    # SPS
    """Get SPS link element"""
    def get_sps_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/a')

    """Get SPS button register element"""
    def get_sps_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[5]/a')

    # PSMII
    """Get PSMII link element"""
    def get_psmii_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/a')

    """Get PSMII button register element"""
    def get_psmii_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[5]/a')

    # EVIDENCE AGIL
    """Get EVIDENCE AGIL link element"""
    def get_evidence_agil_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[1]/a')

    """Get EVIDENCE AGIL button register element"""
    def get_evidence_agil_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[5]/a')

    ##
    """Get CONTACTUS button register element"""
    def get_request_custom_training_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[2]/div[1]/div/a')

    """Get VIEW ALL UPCOMING TRAININGS BTN"""
    def get_view_all_upcoming_trainings_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[2]/div[2]/div/a')

    """Get INTRO TO AGILE link emement"""
    def get_intro_to_agile_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[1]/div/div/ul/li/div[2]/div/h2[3]/a')

    """Get CONTACTUS button2 register element"""
    def get_request_agil_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[1]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get PSF link emement"""
    def get_psf_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[2]/div[1]/div/ul/li/div[2]/div[2]/h2[4]/a')

    """Get CONTACTUS button3 register element"""
    def get_request_psf_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[2]/div[1]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PSD link emement"""
    def get_psd_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[3]/div[1]/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get CONTACTUS button4 register element"""
    def get_request_psd_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[3]/div[1]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PSM link2 emement"""
    def get_psm_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[4]/div[1]/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get PSM button2 register element"""
    def get_psm_register_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[3]/div[4]/div[1]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PSMII link2 emement"""
    def get_psmii_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[1]/div[2]/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get PSMII button2 register element"""
    def get_psmii_register_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[1]/div[2]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PSPO link2 emement"""
    def get_pspo_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[2]/div[2]/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get PSPO button2 register element"""
    def get_pspo_register_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[2]/div[2]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get SPS link2 emement"""
    def get_sps_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[3]/div[2]/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get SPS button2 register element"""
    def get_sps_register_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[3]/div[2]/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PAL E link emement"""
    def get_pal_e_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[4]/div/div/ul/li/div[2]/div/h2[3]/a')

    """Get CONTACTUS button5 register element"""
    def get_request_pal_e_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[4]/div[4]/div/div/ul/li/div[2]/div/p[2]/a')

    """Get EVIDENCE BASE AGILITY link2 emement"""
    def get_evidence_base_agility_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[1]/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get EVIDENCE BASE AGILITY button2 register element"""
    def get_evidence_base_agility_register_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[1]/div/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get KANBA SYSTEM DESIGN link emement"""
    def get_kanba_system_design_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[2]/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get CONTACTUS button6 register element"""
    def get_request_kanba_s_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[2]/div/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get KANBA MANAGEMENT PROF link emement"""
    def get_kanba_management_prof_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[3]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button7 register element"""
    def get_request_kanba_m_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[3]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get TEAM KANBAN PRACTITIONER link emement"""
    def get_team_kanban_practitioner_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[4]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button8 register element"""
    def get_request_kanba_p_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[5]/div[4]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get PSK link emement"""
    def get_psk_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[1]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button9 register element"""
    def get_request_psk_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[1]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get M3 0 link emement"""
    def get_m3_0_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[2]/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get CONTACTUS button10 register element"""
    def get_request_m30_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[2]/div/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get PSU link emement"""
    def get_psu_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[3]/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get CONTACTUS button11 register element"""
    def get_request_psu_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[4]/div[6]/div[3]/div/div/ul/li/div[2]/div[2]/p[2]/a')

    """Get AGILE PRACTICES AND TOOLS link emement"""
    def get_agile_practices_and_tools_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[5]/div[1]/div/div/h1/a')

    """Get BDD link emement"""
    def get_bdd_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[5]/div[2]/div[2]/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get CONTACTUS button12 register element"""
    def get_request_bdd_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[5]/div[2]/div[2]/div/div/ul/li/div[2]/div[2]/p[3]/a')

    """Get AGILE TESTING WORKSHOP link emement"""
    def get_agile_testing_workshop_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[5]/div[2]/div[3]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button13 register element"""
    def get_request_agiltesting_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[5]/div[2]/div[3]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get AGILE CULTURE link emement"""
    def get_agile_culture_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[1]/div/div/h1/span/a')

    """Get AGILE DIVERSITY link emement"""
    def get_agile_diversity_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[1]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button14 register element"""
    def get_request_agildiverity_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[1]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get AGILE CONFLICT link emement"""
    def get_agile_conflict_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[2]/div/div/ul/li/div[2]/div/h2[1]/a')

    """Get CONTACTUS button15 register element"""
    def get_request_agilconflict_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[2]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get AGILE MOTIVATION link emement"""
    def get_agile_motivation_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[3]/div/div/ul/li/div[2]/div/h2[1]/a')

    """Get CONTACTUS button16 register element"""
    def get_request_agilmotivation_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[3]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get AGILE CHANGE link emement"""
    def get_agile_change_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[4]/div/div/ul/li/div[2]/div/h2[2]/a')

    """Get CONTACTUS button17 register element"""
    def get_request_agilchanges_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[2]/div[4]/div/div/ul/li/div[2]/div/p[3]/a')

    """Get CONTACTUS button18 register element"""
    def get_request_ct_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[5]/div/div[2]/h1/a')

    """Get CONTACTUS button19 register element"""
    def get_request_req_ct_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[6]/div[5]/div/div[3]/a')

    """Get VIEW ALL UPCOMING TRAININGS BTN2"""		
    def get_view_all_upcoming_trainings_btn2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[1]/div/div/h1/a')

    """Get CONTACTUS button20 register element"""
    def get_request_uncoming_t_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[2]/div[1]/div/a')

    """Get VIEW ALL UPCOMING TRAININGS BTN3"""		
    def get_view_all_upcoming_trainings_btn3(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[2]/div[2]/div/a')

    """Get AGILE DEVOPS MEETUP link emement"""
    def get_agile_devops_meetup_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[3]/div/div/div/ul/li[1]/div[2]/div[2]/h2[3]/a')

    """Get AGILE DEVOPS MEETUP button register element"""
    def get_agile_devops_meetup_register_btn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[3]/div/div/div/ul/li[1]/div[2]/div[2]/p[3]/a')

    """Get SCCRUM PULSE WEBINAR link emement"""
    def get_scrum_pulse_webinar_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[3]/div/div/div/ul/li/div[2]/div[2]/h2[3]/a')

    """Get SCRUM PULSE WEBINAR link2 emement"""		
    def get_scrum_pulse_webinar_link2(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[7]/div[3]/div/div/div/ul/li/div[2]/div[2]/p[3]/a')
