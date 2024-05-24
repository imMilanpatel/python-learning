# Imports
import pytest
from playwright.sync_api import sync_playwright, expect
from ..utilities import site_cred
from ..POM import login_page

@pytest.fixture(scope="session")
def browser():
    # Initialize browser instance
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser in headed mode
        yield browser
        # Close the browser after all tests are finished
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    # Create a new page for each test
    page = browser.new_page()
    yield page
    # Close the page after the test
    page.close()

def test_login(page):
    # Your test function
    page.goto(site_cred.site_url)
    
    page.get_by_label(login_page.username_box).fill(site_cred.username)

    page.get_by_label(login_page.password_box).fill(site_cred.password)
    
    page.get_by_role("button", name=login_page.login_button).click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("li").filter(has_text="John Smith")).to_be_visible()