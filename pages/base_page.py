from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def expect_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()
