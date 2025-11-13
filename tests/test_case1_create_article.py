from pages.article_page import ArticlePage
from utils.api_helper import create_article
from utils.data_generator import random_string


def test_create_article_via_api_after_ui_login(page):
    page.goto("https://conduit.bondaracademy.com/")

    token = page.evaluate("() => window.localStorage.getItem('jwtToken')")
    assert token, "Token not found in browser localStorage"
    print("Auth token successfully fetched from saved session")

    title = f"Hybrid_API_Article_{random_string()}"
    desc = f"This is about article created via API after UI login {random_string()}"
    body = f"This is the body of the hybrid test article {random_string()}"
    tags = ["api", "hybrid", "playwright", "mehedi"]

    article = create_article(token, title, desc, body, tags)
    print(f"Article created via API: {article['slug']}")

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    article_page = ArticlePage(page)
    article_page.expect_title_visible(title)
    page.screenshot(path="screenshots/article_created_via_api_after_ui.png")
    print("Article created successfully via API after UI login")
