import pytest
from playwright.sync_api import sync_playwright
import time

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

def test_case_1(page):
    # Test Case 1 code
    page.goto("https://github.com/imMilanpatel")
    time.sleep(5)
    assert page.title() == "Example Domain"

def test_case_2(page):
    # Test Case 2 code
    page.goto("https://www.google.com")
    time.sleep(5)
    assert page.title() == "Google"

def test_case_3(page):
    # Test Case 3 code
    page.goto("https://www.wikipedia.org")
    time.sleep(5)
    assert page.title() == "Wikipedia"