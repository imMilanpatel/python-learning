#FIXME: This file needs some more changes inorder to run it smoothly.You can refer this for template.
# This is sample test which tests few functionality of the Amazon's E-Commerce site.

import pytest
from playwright.async_api import async_playwright

# Constants
url = 'https://www.amazon.in'
username = 'Your Username'
password = 'Your Password'

@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.mark.asyncio
async def test_amazon_login(browser):
    page = await browser.new_page()
    await page.goto(f'{url}')

    # Check whether the page is loaded correctly or not
    search_input = await page.query_selector('input[id="twotabsearchtextbox"]')
    assert search_input is not None, "Search input element not found on the page"

    # Login Page
    login_link = await page.query_selector('#nav-link-accountList')
    await login_link.click()

    # Replace 'your_username' and 'your_password' with your actual Amazon login credentials
    await page.fill(f'input[id="ap_email"]', '{username}')  # Enter username
    await page.click('input[id="continue"]')  # Click continue button
    await page.fill(f'input[id="ap_password"]', '{password}')  # Enter password
    await page.click('input[id="signInSubmit"]')  # Click sign-in button

    # Optional: You can add an assertion to check if a specific element appears after successful login
    greeting_element = await page.wait_for_selector('#nav-link-accountList-nav-line-1', timeout=10000)
    assert greeting_element is not None, "Login unsuccessful, greeting element not found"

    # Example validation: Check if the user is logged in
    assert "Hello, Sign in" not in await page.title()

@pytest.mark.asyncio
async def test_product_checkout(browser):
    page = await browser.new_page()
    await page.goto(f'{url}')

    # TODO: Add steps to search for a product and add it to the cart
    # Search for a product and add it to the cart (simplified example)
    search_input = await page.query_selector('input[name="field-keywords"]')
    await search_input.fill('asus')  # Replace 'your_product_name' with the actual product name
    await page.press('input[name="field-keywords"]', 'Enter')

    # Click on the first product (assuming the search result is displayed)
    product_link = await page.query_selector('.s-search-results .s-result-item a')
    await product_link.click()

    # Add the product to the cart
    add_to_cart_button = await page.query_selector('#add-to-cart-button')
    await add_to_cart_button.click()

    # Wait for the cart icon to update with a timeout of 10 seconds
    cart_icon = await page.wait_for_selector('#nav-cart-count', timeout=10000)
    assert cart_icon is not None, "Product not added to the cart successfully"

    # Example validation: Check if the product is added to the cart
    #await page.click('button[data-asin="YOUR_PRODUCT_ASIN"]')
    #assert "1 item in your cart" in await page.title()

    # TODO: Add steps to perform checkout action

    # Example validation: Check if the checkout is successful
    #assert "Thank you for your purchase" in await page.title()

@pytest.mark.asyncio
async def test_search_functionality(browser):
    page = await browser.new_page()
    await page.goto(f'{url}')

    # TODO: Add steps to perform a search

    # Example validation: Check if search results are displayed
    await page.type('input[name="field-keywords"]', 'your search query')
    await page.press('input[name="field-keywords"]', 'Enter')
    assert "Search results for" in await page.title()

@pytest.mark.asyncio
async def test_wishlist_functionality(browser):
    page = await browser.new_page()
    await page.goto(f'{url}')

    # TODO: Add steps to add a product to the wishlist

    # Example validation: Check if the product is added to the wishlist
    await page.click('button[aria-label="Add to Wish List"]')
    assert "1 item added to Wish List" in await page.title()

    # TODO: Validate product wishlist functionality

    # Example validation: Check if the wishlist page displays the added product
    await page.goto('https://www.amazon.com/gp/registry/wishlist/')
    assert "YOUR_ADDED_PRODUCT_TITLE" in await page.title()
