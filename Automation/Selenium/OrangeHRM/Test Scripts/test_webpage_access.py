# This file will test out the access to the webpage of the site under test

from selenium import webdriver
from selenium import webdriver

class TestSiteAccess:
    def __init__(self):
        # Set the path of the chromedriver executable
        self.driver = webdriver.Chrome()

    def visit_url(self):
        # Visit the URL
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

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
              