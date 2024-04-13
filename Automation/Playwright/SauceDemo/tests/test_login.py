
# Imports
import pytest
from playwright.sync_api import sync_playwright, expect
from ..POM import login_page_elements
from ..Utilities import credentials


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

# Username and password field input boxes and credentials passing template function for resuability
def template(page,index):
    page.locator(login_page_elements.username_input_box).fill(credentials.accepted_users[index])
    page.locator(login_page_elements.password_input_box).fill(credentials.password)   
    page.locator(login_page_elements.login_button).click()
    

# Common Validations
def successful_login(page):

    #Assertion based on page title
   expect(page.get_by_text("Swag Labs")).to_be_visible()
    

######################################## 

# Actual tests

# Test 1
def test_standard_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=0)
    
    page.wait_for_load_state('networkidle')

    successful_login(page)


# Test 2
def test_locked_out_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=1)
    
    page.wait_for_load_state('networkidle')

    #Assertion
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("svg").first).to_be_visible()
    expect(page.locator("svg").nth(1)).to_be_visible()


# Test 3
def test_problem_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=2)
    
    page.wait_for_load_state('networkidle')

    successful_login(page)


# Test 4
def test_performance_glitch_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=3)
    
    page.wait_for_load_state('networkidle')

    successful_login(page)


# Test 5
def test_error_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=4)
    
    page.wait_for_load_state('networkidle')

    successful_login(page)


# Test 6
def test_visual_user_login(page):
    page.goto(credentials.url)
    page.wait_for_load_state('networkidle')

    template(page, index=5)
    
    page.wait_for_load_state('networkidle')

    successful_login(page)