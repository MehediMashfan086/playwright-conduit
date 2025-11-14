from playwright.sync_api import expect

from pages.base_page import BasePage


class ArticlePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_link = page.get_by_role("link", name="Sign in")
        self.new_article_link = page.get_by_role("link", name="New Article")

        self.title_input = page.get_by_placeholder("Article Title")
        self.desc_input = page.get_by_placeholder("What's this article about?")
        self.body_input = page.get_by_placeholder("Write your article (in markdown)")
        self.tags_input = page.get_by_placeholder("Enter tags")

        self.publish_button = page.get_by_role("button", name="Publish Article")

        self.article_title = page.locator("article h1").or_(page.locator("h1"))

        actions = page.locator("div.article-actions")
        self.edit_button = actions.get_by_role("link", name="Edit Article").first
        self.delete_button = actions.get_by_role("button", name="Delete Article").first

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
        expect(self.page).to_have_url(
            "https://conduit.bondaracademy.com/", timeout=10000
        )
        expect(self.page.locator("div.home-page")).to_be_visible(timeout=10000)
        expect(self.page.get_by_text("Popular Tags")).to_be_visible(timeout=10000)

    def expect_title_visible(self, title):
        expect(self.article_title).to_be_visible(timeout=10000)
        expect(self.article_title).to_have_text(title, timeout=20000)
