# This file will check whether the login functionality is working fine or not.
# OrangeHRM Demo site is used to demonstrate this.

# Imports
import pytest
from playwright.sync_api import sync_playwright


# Constants
url = ""
username = ""
password = ""

# Pytest fixtures
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# Function defintions (Acutal tests)

def test_login(page):
    # Step 1 Navigate to URL
    # Step 2 Input Username
    # Step 3 Input Password
    # Click Login button
    # Validate Successful login
    pass