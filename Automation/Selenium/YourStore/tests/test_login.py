from selenium import webdriver
from utilities import site_cred
import time

def test_login():
    chrome_browser = webdriver.Chrome()
    chrome_browser.get(site_cred.site_url)
    time.sleep(5)
    chrome_browser.quit()
