from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Resolve locator string OR locator object
    def _resolve(self, target):
        if isinstance(target, Locator):
            return target
        return self.page.locator(target)

    def visit(self, url: str):
        self.page.goto(url)

    def click(self, target, timeout=8000):
        element = self._resolve(target)
        element.wait_for(state="visible", timeout=timeout)
        element.click()

    def fill(self, target, value, timeout=8000):
        element = self._resolve(target)
        element.wait_for(state="visible", timeout=timeout)
        element.fill(value)

    def expect_visible(self, target, timeout=8000):
        element = self._resolve(target)
        expect(element).to_be_visible(timeout=timeout)

    def get_text(self, target):
        element = self._resolve(target)
        element.wait_for(state="visible")
        return element.inner_text()
