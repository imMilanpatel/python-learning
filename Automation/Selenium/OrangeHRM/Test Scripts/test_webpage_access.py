# This file will test out the access to the webpage of the site under test

from selenium import webdriver
from Utilities import Website_Config
import time

class TestSiteAccess:

    def setup(self):
        driver = webdriver.Chrome()
        return driver
    
    def open_app(self):
        self.driver.get(Website_Config.Credentials.site_link) 
        time.wait(5)

    def teardown(self):
        self.driver.quit() 
              