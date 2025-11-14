from pages.article_page import ArticlePage
from utils import logger
from utils.api_helper import create_article
from utils.data_generator import random_string

log = logger.get_logger()


def test_delete_article_after_api_creation(page):
    page.goto("https://conduit.bondaracademy.com/")
    token = page.evaluate("() => window.localStorage.getItem('jwtToken')")
    assert token, "Token not found in browser localStorage"
    log.info(".... Reused authenticated session successfully ....")

    title = f"Deletable_Article_{random_string()}"
    desc = f"Precondition article created via API {random_string()}"
    body = f"Initial body for article {random_string()}"
    tags = ["api", "delete", "playwright"]

    article = create_article(token, title, desc, body, tags)
    log.info(f".... Article created via API: {article['slug']} ....")

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    article_page = ArticlePage(page)
    article_page.expect_title_visible(title)

    article_page.delete_article_ui()
    log.info(".... Delete button clicked ....")

    article_page.expect_article_deleted()
    log.info(".... Redirected to home page successfully ....")

    page.screenshot(path="screenshots/article_deleted_via_ui.png")
    log.info(".... DELETE ARTICLE SUCCESSFULLY ....")
