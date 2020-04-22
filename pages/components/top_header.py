from webium import Find
from selenium.webdriver.common.by import By

class TopHeader(object):
    facebookIcon = Find(by=By.CSS_SELECTOR, value='#et-secondary-menu > ul.et-social-icons > li.et-social-icon.et-social-facebook')
    twitterIcon = Find(by=By.CSS_SELECTOR, value='#et-secondary-menu > ul.et-social-icons > li.et-social-icon.et-social-twitter')
    googleIcon = Find(by=By.CSS_SELECTOR, value='#et-secondary-menu > ul.et-social-icon > li.et-social-google-plus')
    linkedinIcon = Find(by=By.CSS_SELECTOR, value='#et-secondary-menu > ul.et-social-icons > li.et-social-icon.et-social-linkedin')
    rssIcon = Find(by=By.CSS_SELECTOR, value='#et-secondary-menu > ul.et-social-icons > li.et-social-icon.et-social-rss')
    contactUs = Find(by=By.CSS_SELECTOR, value='#et-secondary-nav > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-4912 > a')
    phone = Find(by=By.CSS_SELECTOR, value='#et-info-phone')
    email = Find(by=By.CSS_SELECTOR, value='#et-info-email')