from pages.article_page import ArticlePage
from utils import logger
from utils.api_helper import create_article
from utils.data_generator import random_string

log = logger.get_logger()


def test_edit_article_after_api_creation(page):
    page.goto("https://conduit.bondaracademy.com/")
    token = page.evaluate("() => window.localStorage.getItem('jwtToken')")
    assert token, "Token not found in browser localStorage"

    title = f"Editable_Article_{random_string()}"
    desc = f"Precondition article created via API {random_string()}"
    body = f"Initial body for article {random_string()}"
    tags = ["api", "edit", "playwright"]

    article = create_article(token, title, desc, body, tags)
    log.info(f".... Article created via API: {article['slug']} ....")

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    article_page = ArticlePage(page)

    new_title = f"Edited_{random_string()}"
    new_desc = f"Updated description {random_string()}"
    new_body = f"Edited article body content {random_string()}"

    article_page.edit_article_ui(new_title, new_desc, new_body)
    article_page.expect_title_visible(new_title)

    page.screenshot(path="screenshots/article_edited_via_ui.png")
    log.info(".... Edited article verified successfully! ....")
