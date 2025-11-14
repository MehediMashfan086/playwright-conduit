from pages.base_page import BasePage
from utils import logger

log = logger.get_logger()


class SettingsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.settings_text = "a:has-text('Settings')"
        self.settings_link = "a[href='/settings']"
        self.url_of_pp_input = "input[placeholder='URL of profile picture']"
        self.username_input = "input[placeholder='Username']"
        self.short_bio_input = "textarea[placeholder='Short bio about you']"
        self.email_input = "input[placeholder='Email']"
        self.new_password_input = "input[placeholder='New Password']"
        self.update_settings_button = "button:has-text('Update Settings')"
        self.update_settings_done_text = "a:has-text('My Posts')"

    def go_to_home(self):
        self.visit("https://conduit.bondaracademy.com/")
        self.expect_visible(self.settings_text)
        log.info(".... Logged in successfully using saved session ....")

    def navigate(self):
        self.click(self.settings_link)

    def update_settings(self, url_of_pp, username, short_bio, email, new_password):
        self.fill(self.url_of_pp_input, url_of_pp)
        self.fill(self.username_input, username)
        self.fill(self.short_bio_input, short_bio)
        self.fill(self.email_input, email)
        self.fill(self.new_password_input, new_password)
        self.click(self.update_settings_button)
        log.info(".... Settings update submitted ....")

    def expect_settings_update_done(self):
        self.expect_visible(self.update_settings_done_text)
        log.info(".... Settings updated successfully ....")
