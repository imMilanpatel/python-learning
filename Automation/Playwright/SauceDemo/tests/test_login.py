
# Imports
import pytest
from playwright.sync_api import sync_playwright, expect
from ..POM import login_page_elements
from ..Utilities import credentials
import time

# Browser defintion
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()

# Page definition
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

######################################## 

# Actual tests

def test_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    page.locator(login_page_elements.username_input_box).fill(credentials.accepted_users[0])
    time.sleep(2)
    page.locator(login_page_elements.password_input_box).fill(credentials.password)
    time.sleep(2)
    page.locator(login_page_elements.login_button).click()
    time.sleep(2)
    page.wait_for_load_state('networkidle')
