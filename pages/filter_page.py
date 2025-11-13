import random

from playwright.sync_api import expect

from pages.base_page import BasePage


class FilterPage(BasePage):
    tag_list = ".tag-list a"
    feed_toggle = ".feed-toggle li.nav-item a.active"
    article_preview = ".article-preview"
    new_article = "a:has-text('New Article')"

    def go_to_home(self):
        self.visit("https://conduit.bondaracademy.com/")
        self.expect_visible(self.new_article)
        print("Logged in successfully using saved session")

    def select_random_tag(self):
        self.page.wait_for_selector(self.tag_list, timeout=10000)
        tags = self.page.locator(self.tag_list)
        tag_count = tags.count()
        assert tag_count > 0, "No tags found in sidebar"

        random_index = random.randint(0, tag_count - 1)
        tag_text = tags.nth(random_index).inner_text().strip()
        tags.nth(random_index).click()
        print(f"Selected random tag: {tag_text}")
        return tag_text

    def verify_feed_for_tag(self, tag_text):
        selected_feed = self.page.locator(self.feed_toggle)
        actual_text = selected_feed.inner_text().strip()
        assert (
            tag_text.lower() in actual_text.lower()
        ), f"Expected active feed to include tag '{tag_text}', but got '{actual_text}'"
        print(f"Filter applied for tag: {actual_text}")

    def verify_articles_loaded(self):
        articles = self.page.locator(self.article_preview)
        expect(articles.first).to_be_visible(timeout=10000)
        print("Articles loaded successfully under selected tag")

    def take_screenshot(self, tag_text):
        self.page.screenshot(path=f"screenshots/filter_by_tag_{tag_text}.png")
        print(f"Screenshot captured for tag '{tag_text}'")
