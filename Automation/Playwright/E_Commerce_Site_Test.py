# TODO: Implement the below functionality one by one

# Imports
from playwright.sync_api import Playwright, sync_playwright, expect


def amazon_site_basic_tests(playwright: Playwright) -> None:

    # Browser instance
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()

    # Site access
    page.goto("https://www.amazon.in/")
    # FIXME: After login there is small captcha, which needs to be addressed.

    # Login functionality check
    page.get_by_role("link", name="Hello, sign in Account & Lists").click()
    page.get_by_label("Email or mobile phone number").click()
    page.get_by_label("Email or mobile phone number").fill("milanpatel3116@gmail.com")
    page.get_by_label("Continue").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").press("CapsLock")
    page.get_by_label("Password").fill("M")
    page.get_by_label("Password").press("CapsLock")
    page.get_by_label("Password").fill("Milan+3196$")
    page.get_by_label("Sign in").click()

    # Commented out OTP part for future implementation
    #page.locator("#input-box-otp").click()
    #page.locator("#input-box-otp").fill("585186")
    #page.get_by_label("Submit code").click()

    # Validation of successful login
    expect(page.locator("#nav-link-accountList-nav-line-1")).to_contain_text("Hello, Milan")
    expect(page.locator("#nav-global-location-popover-link")).to_contain_text("Deliver to Milan Tiruchira... 620008‌")


    # Search functionality check
    page.get_by_placeholder("Search Amazon.in").fill("laptops")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    expect(page.locator("#search > div").first).to_be_visible()
    expect(page.locator("h1")).to_contain_text("\"laptops\"")

    # FIXME: Wishlist dropdown issue, site says that it is now working at the moment.
    # Wishlist functionality check
    page.mouse.wheel(0,100)  
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Dell 14 Laptop, 12th Gen Intel Core i3-1215U Processor/8GB/512GB SSD/Intel UHD Graphics/14.0\"(35.56cm) FHD/Windows 11 + MSO'21/15 Month McAfee/Spill-Resistant Keyboard/Grey/Thin & Light 1.48kg", exact=True).click()
    page1 = page1_info.value
    expect(page1.get_by_text("Sponsored ‹ Back to results")).to_be_visible()
    page.mouse.wheel(0,200)
    page1.get_by_label("Add to Wish List").click()
    page1.get_by_label("Close", exact=True).click()  

    
    context.close()
    browser.close()
# def test_product_checkout(browser):

with sync_playwright() as playwright:
    amazon_site_basic_tests(playwright)