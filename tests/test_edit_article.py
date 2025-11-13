from pages.article_page import ArticlePage
from pages.login_page import LoginPage
from utils.api_helper import create_article
from utils.data_generator import random_string


def test_edit_article_after_api_creation(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    login_page.expect_logged_in()

    token = login_page.get_auth_token_from_browser()
    assert token, "Token not found in browser localStorage"

    title = f"Editable_Article_{random_string()}"
    desc = f"Precondition article created via API {random_string()}"
    body = f"Initial body for article {random_string()}"
    tags = ["api", "edit", "playwright"]

    article = create_article(token, title, desc, body, tags)
    print(f"Article created via API: {article['slug']}")

    page.goto(f"https://conduit.bondaracademy.com/article/{article['slug']}")
    edit_page = ArticlePage(page)
    new_title = f"Edited_{random_string()}"
    new_desc = f"Updated description {random_string()}"
    new_body = f"Edited article body content {random_string()}"

    edit_page.edit_article_ui(new_title, new_desc, new_body)
    print("Article updated via UI.")

    edit_page.expect_title_visible(new_title)
    print("Edited article verified successfully!")

    page.screenshot(path="screenshots/article_edited_via_ui.png")
    print("....TEST COMPLETED SUCCESSFULLY....")
