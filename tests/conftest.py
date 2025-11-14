import os
import sys

import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import config, logger

log = logger.get_logger()


@pytest.fixture(scope="session", autouse=True)
def ensure_login_state():
    state_dir = "auth"
    state_file = os.path.join(state_dir, "state.json")
    os.makedirs(state_dir, exist_ok=True)

    if os.path.exists(state_file):
        log.info(".... Using existing authenticated session ....")
        return

    log.info(".... Logging in once to create new session....")

    # Determine headless mode (force True in CI)
    if os.getenv("CI"):
        headless = True
    else:
        headless = config.HEADLESS

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://conduit.bondaracademy.com/login")
        page.fill("input[placeholder='Email']", "mehedi_test@gmail.com")
        page.fill("input[placeholder='Password']", "Pass@123")
        page.click("button:has-text('Sign in')")
        page.wait_for_selector("a:has-text('New Article')", timeout=10000)

        context.storage_state(path=state_file)
        log.info(f".... Login successful. Session saved at {state_file} ....")

        browser.close()


@pytest.fixture(scope="session")
def browser():
    if os.getenv("CI"):
        headless = True
    else:
        headless = config.HEADLESS

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True, storage_state="auth/state.json")
    page = context.new_page()
    yield page
    context.close()
