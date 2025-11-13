from playwright.sync_api import expect

from pages.base_page import BasePage


class ArticlePage(BasePage):
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
        self.edit_button = (
            "div.article-actions a.btn.btn-outline-secondary:has-text('Edit Article')"
        )
        self.delete_button = "div.article-actions button.btn.btn-outline-danger"

    def edit_article_ui(self, new_title, new_desc, new_body):
        self.click(self.edit_button)
        self.expect_visible(self.title_input)

        self.fill(self.title_input, new_title)
        self.fill(self.desc_input, new_desc)
        self.fill(self.body_input, new_body)
        self.click(self.publish_button)

    def delete_article_ui(self):
        self.click(self.delete_button)

    def expect_article_deleted(self):
        expect(self.page).to_have_url("https://conduit.bondaracademy.com/")
        expect(self.page.locator("a.nav-link", has_text="Global Feed")).to_be_visible()

    def expect_title_visible(self, title):
        expect(self.page.locator(self.article_title)).to_be_visible(timeout=8000)
        expect(self.page.locator(self.article_title)).to_have_text(title, timeout=8000)
