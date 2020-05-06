import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as chains
from common.utils import Utils

class HomeLocator:
    # Learn More
    def getLearnMoreBtn(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[1]/div/div[2]/div[2]/a')
    #*****UPCOMING TRAININGS
    # PSPO
    def getPspoLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/a')

    def getPspoRegisterLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[5]/a')

    # PSM
    def getPsmLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/a')

    def getPsmRegisterLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/a')

    # SPS
    def getSpsLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/a')

    def getSpsRegisterLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div[5]/a')

    # PSMII
    def getPsmiiLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/a')

    def getPsmiiRegisterLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[4]/div[5]/a')

    # EVIDENCE AGIL
    def getEvidenceAgilLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[1]/a')

    def getEvidenceAgilRegisterLink(self):
        return Utils.find_element_by_xpath(self,'//*[@id="post-39"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[5]/div[5]/a')
