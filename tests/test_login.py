from pages.login_page import LoginPage


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("test_mehedi@gmail.com", "Pass@123")
    login_page.expect_invalid_logged_in()
    login_page.page.screenshot(path="screenshots/invalid_login.png")


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    login_page.expect_logged_in()
    login_page.page.screenshot(path="screenshots/valid_login.png")
