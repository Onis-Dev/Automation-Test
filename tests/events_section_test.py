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
class TestEvents:

    CONST = CONSTANTS['HOME']
    TITLES = CONSTANTS['TITLES_PAGES']
    CONSTHEADER = CONSTANTS['HEADER']
    ELEMENTS = PAGE_ELEMENTS['HOME']

    #AGILE EVENTS
    @allure.title("Test AGILE EVENTS LINK is displayed") 
    @allure.description(" Test if link is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_view_all_upcoming_trainings_btn2
    def test_home_view_all_upcoming_trainings_btn2(self, get_base_url):
        view_all_upcoming_trainings_btn2 = HomeLocator.get_view_all_upcoming_trainings_btn2(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn2), 'AGILE EVENTS LINK is not being displayed'
       
       
    @allure.title("Test RESQUEST A SPEAKER BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_request_uncoming_t_btn
    def test_home_request_uncoming_t_btn(self, get_base_url):
        request_uncoming_t_btn = HomeLocator.get_request_uncoming_t_btn(self)  
        assert Utils.is_displayed(self,request_uncoming_t_btn), 'RESQUEST A SPEAKER BUTTON is not being displayed'
       
       
    @allure.title("Test VIEW ALL UPCOMING EVENTS BUTTON is displayed") 
    @allure.description(" Test if button is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.home_view_all_upcoming_trainings_btn3
    def test_home_view_all_upcoming_trainings_btn3(self, get_base_url):
        view_all_upcoming_trainings_btn3 = HomeLocator.get_view_all_upcoming_trainings_btn3(self)  
        assert Utils.is_displayed(self,view_all_upcoming_trainings_btn3), 'AGILE EVENTS LINK is not being displayed'           


    # @allure.title("Test SCRUM PULSE WEBINAR LINK redirect is displayed and working") 
    # @allure.description(" Test if link is displayed and redirect is correct")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_scrum_pulse_webinar_link
    # def test_home_scrum_pulse_webinar_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     scrum_pulse_webinar_link = HomeLocator.get_scrum_pulse_webinar_link(self)
    #     scrum_pulse_webinar_link_url = self.CONST.get('SCRUM_PULSE_WEBINAR_LINK')
    #     scrum_pulse_webinar_title = self.TITLES.get('SCRUM_PULSE_WEBINAR_TITLE')
    #     assert Utils.is_displayed(self,scrum_pulse_webinar_link), 'SCRUM PULSE WEBINAR LINK is not being displayed'
    #     path = Utils.click_link(self,scrum_pulse_webinar_link, scrum_pulse_webinar_title, scrum_pulse_webinar_link_url,True) 
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     assert path == scrum_pulse_webinar_link_url, 'SCRUM PULSE WEBINAR Link is not working'
        
        
    # @allure.title("Test SCRUM PULSE WEBINAR REGISTER BUTTON redirect is displayed") 
    # @allure.description(" Test if button is displayed")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_scrum_pulse_webinar_btn
    # def test_home_scrum_pulse_webinar_link2(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     scrum_pulse_webinar_link2 = HomeLocator.get_scrum_pulse_webinar_link2(self)
    #     assert Utils.is_displayed(self,scrum_pulse_webinar_link2), 'SCRUM PULSE WEBINAR REGISTER BUTTON is not being displayed'

    #BLOG SECTION
    # @allure.title("Test AGILE GALLERY SLIDER  button is displayed and working") 
    # @allure.description(" Test if AGILE GALLERY slider is working correctly")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.home_agile_gallery_slider
    # def test_home_agile_gallery_slider(self, get_base_url):
    #     slider = HomeLocator.get_agile_gallery_slider(self)
    #     assert Utils.is_displayed(self, slider), "slider content is not being displayed"
    #     slider_titles = HomeLocator.get_agile_gallery_slider_texts(self)
    #     sliderControl = HomeLocator.get_agile_gallery_controllers(self)
    #     page_count = 0
    #     has_text = True
    #     while page_count < len(sliderControl):
    #         sliderControl[page_count].click()
    #         if slider_titles[page_count].get_attribute('text') == None or slider_titles[page_count].get_attribute('text') == "":
    #             has_text = False
    #             break
    #         page_count += 1
    #     assert has_text, "AGILE GALLERY SLIDER is not working correctly"

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


    # @allure.title("Test AGILE VIDEOS IMAGE LINK is displayed and working") 
    # @allure.description(" Test if AGILE VIDEOS IMAGE LINK is working correctly")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_agile_videos_image_link
    # def test_home_agile_videos_image_link(self, get_base_url):
    #     image_link = HomeLocator.get_agile_videos_image_link(self)
    #     image_link_url = get_base_url + self.CONSTHEADER.get('SUBMENU_AGILE_VIDEOS')
    #     assert Utils.is_displayed(self,image_link), "AGILE VIDEOS IMAGE is not being displayed"
    #     path = Utils.click_link(self,image_link, self.TITLES.get('RESOURCES_AGILE_VIDEOS_TITLE'), image_link_url) 
    #     assert path == image_link_url, 'AGILE VIDEOS IMAGE LINK is not working'

    # @allure.title("Test AGILE PRESENTATIONS IMAGE LINK is displayed and working") 
    # @allure.description(" Test if AGILE PRESENTATIONS IMAGE LINK is working correctly")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.home_agile_presentations_image_link
    # def test_home_agile_presentations_image_link(self, get_base_url):
    #     self.driver.get(get_base_url)
    #     image_link = HomeLocator.get_agile_presentations_image_link(self)
    #     image_link_url = get_base_url + self.CONST.get('AGILE_PRESENTATIONS')
    #     assert Utils.is_displayed(self,image_link), "AGILE PRESENTATIONS IMAGE is not being displayed"
    #     path = Utils.click_link(self,image_link, self.TITLES.get('RESOURCES_AGILE_PRESENTATIONS_TITLE'), image_link_url) 
    #     assert path == image_link_url, 'AGILE PRESENTATIONS IMAGE LINK is not working'