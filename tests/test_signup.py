import time

from pages.signup_page import SignUpPage


def test_valid_signup(page):
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate()

    timestamp = int(time.time())
    unique_username = f"testuser_{timestamp}"
    unique_email = f"{unique_username}@gmail.com"

    sign_up_page.signup(unique_username, unique_email, "Pass@123")
    sign_up_page.expect_signed_up()
    sign_up_page.page.screenshot(path="screenshots/valid_signup.png")
