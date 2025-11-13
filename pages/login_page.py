from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "input[placeholder='Email']"
        self.password_input = "input[placeholder='Password']"
        self.login_link = "a[href='/login']"
        self.login_button = "button:has-text('Sign in')"
        self.error_message = "ul.error-messages li"
        self.logged_in_text = "a:has-text('New Article')"

    def navigate(self):
        self.visit("https://conduit.bondaracademy.com")
        self.click(self.login_link)

    def login(self, email, password):
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def expect_invalid_logged_in(self):
        self.get_text(self.error_message)

    def expect_logged_in(self):
        self.expect_visible(self.logged_in_text)
