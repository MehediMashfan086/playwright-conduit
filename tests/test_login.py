from pages.login_page import LoginPage


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("test_mehedi@gmail.com", "Pass@123")
    assert "email or password is invalid" in login_page.get_error_message()
    login_page.page.screenshot(path="screenshots/invalid_login.png")


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    assert login_page.get_logged_in_text()
    login_page.page.screenshot(path="screenshots/valid_login.png")
