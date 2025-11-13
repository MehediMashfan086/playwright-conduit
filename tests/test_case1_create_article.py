import time

from pages.article_page import ArticlePage
from pages.login_page import LoginPage
from utils.api_helper import create_article
from utils.data_generator import random_string


def test_create_article_via_api_after_ui_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    login_page.expect_logged_in()

    token = login_page.get_auth_token_from_browser()
    assert token is not None, "Failed to get token from browser localStorage"

    title = f"Hybrid_API_Article_{random_string()}"
    desc = f"This is about article created via API after UI login {random_string()}"
    body = f"This is the body of the hybrid test article {random_string()}"
    tags = ["api", "hybrid", "playwright", "mehedi"]

    article = create_article(token, title, desc, body, tags)

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    article_page = ArticlePage(page)
    article_page.expect_title_visible(title)

    page.screenshot(path="screenshots/article_created_via_api_after_ui.png")

    print(f"Article created successfully via API after UI login: {article['slug']}")
