from playwright.sync_api import expect

from pages.base_page import BasePage


class CreateArticlePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_link = "a[href='/login']"
        self.new_article_link = "a[href='/editor']"
        self.title_input = "input[placeholder='Article Title']"
        self.desc_input = 'input[placeholder="What\'s this article about?"]'
        self.body_input = "textarea[placeholder='Write your article (in markdown)']"
        self.tags_input = "input[placeholder='Enter tags']"
        self.publish_button = "button:has-text('Publish Article')"
        self.article_title = "h1"

    def create_article_ui(self, title, desc, body, tags):
        self.click(self.new_article_link)
        self.fill(self.title_input, title)
        self.fill(self.desc_input, desc)
        self.fill(self.body_input, body)
        for tag in tags:
            self.fill(self.tags_input, tag)
            self.page.locator(self.tags_input).press("Enter")
        self.click(self.publish_button)

    def expect_title_visible(self, title):
        expect(self.page.locator(self.article_title)).to_be_visible(timeout=8000)
        expect(self.page.locator(self.article_title)).to_have_text(title, timeout=8000)
