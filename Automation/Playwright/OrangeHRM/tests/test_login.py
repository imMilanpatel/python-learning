# This file will check whether the login functionality is working fine or not.
# OrangeHRM Demo site is used to demonstrate this.

# Imports
import pytest
from playwright.sync_api import sync_playwright, expect
from ..POM.login_page import LoginPage

# Pytest fixtures
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="module")
def login_page(page):
    return LoginPage(page)

# Function defintions (Acutal tests)

# Test 1 (Valid Login Test)
def test_login(page,login_page):
    # Step 1 Navigate to URL
    login_page.navigate_to_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_load_state("networkidle")

    # Step 2 Input Username
    login_page.username("Admin")

    # Step 3 Input Password
    login_page.password("admin123")

    # Click Login button
    login_page.click_login_button()

    # Validate Successful login
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")