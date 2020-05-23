import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

"""Class to get all elements from HOME section"""
class TrainingLocator:
         
    """Get CONTACTUS button register element"""
    def get_t_request_custom_training_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_REQUEST_CUSTOM_TRAINING_BTN_XPATH'))
    
    """Get VIEW ALL UPCOMING TRAININGS BTN"""
    def get_t_view_all_upcoming_trainings_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_UPCOMING_TRAINING_BTN_XPATH'))

    """Get CONTACTUS button register element"""
    def get_t_request_ct_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_REQUEST_CUSTOM_TRAINING_BTN2_XPATH'))

    #AGILE FRAMEWORK

    """Get CONTACTUS button register element"""
    def get_af_request_custom_training_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AF_REQUEST_CUSTOM_TRAINING_BTN_XPATH'))
    
    """Get VIEW ALL UPCOMING TRAININGS BTN"""
    def get_af_view_all_upcoming_trainings_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AF_UPCOMING_TRAINING_BTN_XPATH'))

    """Get CONTACTUS button register element"""
    def get_af_request_ct_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AF_REQUEST_CUSTOM_TRAINING_BTN2_XPATH'))


    #AGILE CULTURE PAGE
    """Get REQUESTTRAINING button element"""
    def get_ac_request_training_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('AC_REQUEST_TRAINING_BTN_XPATH'))

    #TEST CONTACT US FORM
    """Get CONTACT US FORM"""
    def get_contactus_container_form(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_CONTAINER_FORM'))

    """Get FORM NAME element"""
    def get_form_name_field(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_FORM_NAME_FIELD'))
    
    """Get FORM EMAIL element"""
    def get_form_email_field(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_FORM_EMAIL_FIELD'))

    """Get FORM COMPANY element"""
    def get_form_company_field(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_FORM_COMPANY_FIELD'))

    """Get FORM MESSAGE element"""
    def get_form_message_field(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_FORM_MESSAGE_FIELD'))

    """Get FORM SUBMIT element"""
    def get_form_submit_btn(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_SUBMIT_BUTTON'))

    """Get FORM NOTIFICATION element"""
    def get_form_notification(self):
        return Utils.find_element_by_xpath(self, self.ELEMENTS.get('T_CONTACTUS_FORM_NOTIFICATION'))

    
