from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").press("CapsLock")
    page.get_by_placeholder("Username").fill("A")
    page.get_by_placeholder("Username").press("CapsLock")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("span").filter(has_text="123Test 92Test 80 Bo nie")).to_be_visible()
    page.locator("span").filter(has_text="123Test 92Test 80 Bo nie").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
