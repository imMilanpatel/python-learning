import pytest
from playwright.sync_api import sync_playwright
import time

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_amazon_login(browser):
    page = browser.new_page()
    page.goto('https://www.amazon.in')

    # Check whether the page is loaded correctly or not
    search_input = page.query_selector('input[id="twotabsearchtextbox"]')
    assert search_input is not None, "Search input element not found on the page"

    # Login Page
    login_link = page.query_selector('#nav-link-accountList')
    login_link.click()

    # Replace 'your_username' and 'your_password' with your actual Amazon login credentials
    page.fill('input[id="ap_email"]', '')  # Enter username
    page.click('input[id="continue"]')  # Click continue button
    page.fill('input[id="ap_password"]', '')  # Enter password
    page.click('input[id="signInSubmit"]')  # Click sign-in button

    # Optional: You can add an assertion to check if a specific element appears after successful login
    greeting_element = page.wait_for_selector('#nav-link-accountList-nav-line-1', timeout=10000)
    assert greeting_element is not None, "Login unsuccessful, greeting element not found"

    # Example validation: Check if the user is logged in
    assert "Hello, Sign in" not in page.title()

'''
def test_product_checkout(browser):
    page = browser.new_page()
    page.goto('https://www.amazon.com')

    # TODO: Add steps to search for a product and add it to the cart

    # Example validation: Check if the product is added to the cart
    page.click('button[data-asin="YOUR_PRODUCT_ASIN"]')
    assert "1 item in your cart" in page.title()

    # TODO: Add steps to perform checkout action

    # Example validation: Check if the checkout is successful
    assert "Thank you for your purchase" in page.title()

def test_search_functionality(browser):
    page = browser.new_page()
    page.goto('https://www.amazon.com')

    # TODO: Add steps to perform a search

    # Example validation: Check if search results are displayed
    page.type('input[name="field-keywords"]', 'your search query')
    page.press('input[name="field-keywords"]', 'Enter')
    assert "Search results for" in page.title()

def test_wishlist_functionality(browser):
    page = browser.new_page()
    page.goto('https://www.amazon.com')

    # TODO: Add steps to add a product to the wishlist

    # Example validation: Check if the product is added to the wishlist
    page.click('button[aria-label="Add to Wish List"]')
    assert "1 item added to Wish List" in page.title()

    # TODO: Validate product wishlist functionality

    # Example validation: Check if the wishlist page displays the added product
    page.goto('https://www.amazon.com/gp/registry/wishlist/')
    assert "YOUR_ADDED_PRODUCT_TITLE" in page.title() '''