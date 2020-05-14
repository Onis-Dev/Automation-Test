import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_locator import HomeLocator
from common.environment import CONSTANTS, PAGE_ELEMENTS
from common.utils import Utils


@pytest.mark.usefixtures("setup")
class TestPartners:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']
    ELEMENTS = PAGE_ELEMENTS['HOME']

     #AGILE PARTNERS

    @allure.title("Test AGILE PARTNERS LINK is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_agile_partners_link
    def test_agile_partners_link(self, get_base_url):
        agile_partners_link = HomeLocator.get_agile_partners_link(self)
        learn_more_url = get_base_url + self.CONST.get('AGILE_PARTNERS_LINK')
        learn_more_title = self.TITLES.get('AGILE_PARTNERS_TITLE')
        assert Utils.is_displayed(self,agile_partners_link), 'AGILE PARTNERS LINK is no being displayed'
        path = Utils.click_link(self,agile_partners_link, learn_more_title, learn_more_url) 
        assert path == learn_more_url, 'AGILE PARTNERS REDIRECT is not working'


    @allure.title("Test READ MORE RAVI VERMA BUTTON is displayed and working") 
    @allure.description(" Test if button is displayed and redirect is correct")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_ravi_btn
    def test_read_more_ravi_btn(self, get_base_url):
        self.driver.get(get_base_url)
        read_more_ravi_btn = HomeLocator.get_read_more_ravi_btn(self)
        assert Utils.is_displayed(self,read_more_ravi_btn), 'READ MORE RAVI VERMA BUTTON is no being displayed'
           

    @allure.title("Test READ MORE MARK NONEMAN BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_mark_btn
    def test_home_read_more_mark_btn(self, get_base_url):
        read_more_mark_btn = HomeLocator.get_read_more_mark_btn(self)
        assert Utils.is_displayed(self,read_more_mark_btn), 'READ MORE MARK NONEMAN  BUTTON is not being displayed'
        
        
    @allure.title("Test READ MORE CHARLES BRADLEY BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_charles_b_btn
    def test_home_read_more_charles_b_btn(self, get_base_url):
        read_more_charles_b_btn = HomeLocator.get_read_more_charles_b_btn(self)
        assert Utils.is_displayed(self,read_more_charles_b_btn), 'READ MORE CHARLES BRADLEY BUTTON is not being displayed'   


    @allure.title("Test READ MORE CHARLES SUSCHECK BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_charles_s_btn
    def test_home_read_more_charles_s_btn(self, get_base_url):
        read_more_charles_s_btn = HomeLocator.get_read_more_charles_s_btn(self)
        assert Utils.is_displayed(self,read_more_charles_s_btn), 'READ MORE CHARLES SUSCHECK  BUTTON is not being displayed'
        
        
    @allure.title("Test READ MORE HIREN BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_hiren_btn
    def test_home_read_more_hiren_btn(self, get_base_url):
        read_more_hiren_btn = HomeLocator.get_read_more_hiren_btn(self)
        assert Utils.is_displayed(self,read_more_hiren_btn), 'READ MORE HIREN BUTTON is not being displayed'
           
        
    @allure.title("Test READ MORE RICH VISOTCKY BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_rich_btn
    def test_home_read_more_rich_btn(self, get_base_url):
        read_more_rich_btn = HomeLocator.get_read_more_rich_btn(self)
        assert Utils.is_displayed(self,read_more_rich_btn), 'READ MORE RICH VISOTCKY  BUTTON is not being displayed'
        
        
    @allure.title("Test READ MORE JULEE BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_julee_btn
    def test_home_read_more_julee_btn(self, get_base_url):
        read_more_julee_btn = HomeLocator.get_read_more_julee_btn(self)
        assert Utils.is_displayed(self,read_more_julee_btn), 'READ MORE JULEE BUTTON is not being displayed'
           
        
    @allure.title("Test READ MORE MAGDALENA BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_magdalena_btn
    def test_home_read_more_magdalena_btn(self, get_base_url):
        read_more_magdalena_btn = HomeLocator.get_read_more_magdalena_btn(self)
        assert Utils.is_displayed(self,read_more_magdalena_btn), 'READ MORE MAGDALENA BUTTON is not being displayed'
        
        
    @allure.title("Test READ MORE JILL BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_jill_btn
    def test_home_read_more_jill_btn(self, get_base_url):
        read_more_jill_btn = HomeLocator.get_read_more_jill_btn(self)
        assert Utils.is_displayed(self,read_more_jill_btn), 'READ MORE JILL BUTTON is not being displayed'
           
        
    @allure.title("Test READ MORE NAGESH BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.home_read_more_nagesh_btn
    def test_read_more_nagesh_btn(self, get_base_url):
        read_more_nagesh_btn = HomeLocator.get_read_more_nagesh_btn(self)
        assert Utils.is_displayed(self,read_more_nagesh_btn), 'READ MORE NAGESH BUTTON is not being displayed'
        