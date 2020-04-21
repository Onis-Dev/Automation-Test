from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1400,600")


# @pytest.fixture(scope="session")
# def driver_get(request):
#     print('something?')
#     web_driver = webdriver.Chrome(executable_path="D:\Documentos\Development\Automation\/tests\chromedriver.exe", chrome_options=chrome_options)
#     session = request.node
#     for item in session.items:
#         cls = item.getparent(pytest.Class)
#         setattr(cls.obj,"driver",web_driver)
#     yield
#     web_driver.close()


@pytest.fixture(scope="class")
def driver_init(request):
    x = datetime.now()
    # web_driver = webdriver.Chrome(executable_path="D:\Documentos\Development\Automation\/tests\chromedriver.exe", chrome_options=chrome_options)
    web_driver = webdriver.Chrome(chrome_options=chrome_options)
    request.cls.driver = web_driver
    print('time driver_init {}'.format(datetime.now() - x))
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

@allure.severity(allure.severity_level.MINOR)
class TestHRM(BaseTest):
    def test_Logo(self):
        # wait = WebDriverWait(self.driver, 3)
        x = datetime.now()
        self.driver.get("https://smoothapps.com/")
        status = self.driver.find_element_by_xpath("//*[@id='logo']").is_displayed()
        print('time test_logo {}'.format(datetime.now() - x))
        if status==True:
            assert True
        else:
            assert False
        # self.driver.close()

    def test_email(self):
        # wait = WebDriverWait(self.driver, 3)
        x = datetime.now()
        self.driver.get("https://smoothapps.com/")
        status = self.driver.find_element_by_xpath("//*[@id='et-info-email']")
        print('time test_email {}'.format(datetime.now() - x))
        if status.is_displayed():
            assert True
        else:
            assert False

    def test_contact_us(self):
        x = datetime.now()
        self.driver.get("https://smoothapps.com/")
        textContent = self.driver.find_element_by_xpath("//*[@id='et-secondary-nav']/li[1]/a")
        print('time test_contact_us {}'.format(datetime.now() - x))
        if textContent.text=='ERROR':
            assert True
        else:
            assert False