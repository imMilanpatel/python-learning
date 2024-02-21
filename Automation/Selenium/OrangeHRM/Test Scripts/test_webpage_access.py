# This file will test out the access to the webpage of the site under test

# Imports
from selenium import webdriver

# Test Class
class TestSiteAccess:

    # To initialize the chrome browser driver
    def __init__(self):
        # Set the path of the chromedriver executable
        self.driver = webdriver.Chrome()

    #FIXME: This function needs to get variable from other file
    # To visit site
    def visit_url(self):
        # Visit the URL
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # To close 
    def close_browser(self):
        # Close the browser
        self.driver.close()

    def run(self):
        self.visit_url()
        self.close_browser()

if __name__ == '__main__':
    test_site_access = TestSiteAccess()
    test_site_access.run()
class TestSiteAccess:
    # To be done
    pass
              