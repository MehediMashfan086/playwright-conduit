import time

from pages.article_page import ArticlePage
from pages.login_page import LoginPage
from utils.api_helper import create_article
from utils.data_generator import random_string


def test_delete_article_after_api_creation(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    login_page.expect_logged_in()
    print("Logged in via UI")

    token = login_page.get_auth_token_from_browser()
    assert token, "Token not found in browser localStorage"
    print("Token fetched successfully")

    title = f"Deletable_Article_{random_string()}"
    desc = f"Precondition article created via API {random_string()}"
    body = f"Initial body for article {random_string()}"
    tags = ["api", "delete", "playwright"]

    article = create_article(token, title, desc, body, tags)
    print(f"Article created via API: {article['slug']}")

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    article_page = ArticlePage(page)
    article_page.expect_title_visible(title)

    article_page.delete_article_ui()
    print("Delete button clicked")

    article_page.expect_article_deleted()
    print("Redirected to home page successfully")

    page.screenshot(path="screenshots/article_deleted_via_ui.png")
    print(".... TEST COMPLETED SUCCESSFULLY ....")
