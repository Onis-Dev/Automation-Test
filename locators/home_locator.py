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
    def get_pspo_register_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[5]/a')

    # PSM
    """Get PSM link element"""
    def get_psm_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/a')

    """Get PSM button register element"""
    def get_psm_register_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/a')

    # SPS
    """Get SPS link element"""
    def get_sps_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/a')

    """Get SPS button register element"""
    def get_sps_register_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[5]/a')

    # PSMII
    """Get PSMII link element"""
    def get_psmii_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/a')

    """Get PSMII button register element"""
    def get_psmii_register_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[5]/a')

    # EVIDENCE AGIL
    """Get EVIDENCE AGIL link element"""
    def get_evidence_agil_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[1]/a')

    """Get EVIDENCE AGIL button register element"""
    def get_evidence_agil_register_link(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[5]/a')
