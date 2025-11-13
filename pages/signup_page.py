from pages.base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_link = "a[href='/register']"
        self.username_input = "input[placeholder='Username']"
        self.email_input = "input[placeholder='Email']"
        self.password_input = "input[placeholder='Password']"
        self.signup_button = "button:has-text('Sign up')"
        self.signed_up_text = "a:has-text('New Article')"

    def navigate(self):
        self.visit("https://conduit.bondaracademy.com/")
        self.click(self.signup_link)

    def signup(self, username, email, password):
        self.fill(self.username_input, username)
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.signup_button)

    def expect_signed_up(self):
        self.expect_visible(self.signed_up_text)
