from pages.create_article_page import CreateArticlePage
from pages.login_page import LoginPage
from utils.data_generator import random_string


def test_create_article(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("mehedi_test@gmail.com", "Pass@123")
    login_page.expect_logged_in()

    create_article = CreateArticlePage(page)
    title = f"Article_By_Mehedi_{random_string()}"
    desc = f"This is about of the article {random_string()}"
    body = f"This is body of the article {random_string()}"
    tags = ["playwright", "python", "mehedi"]
    create_article.create_article_ui(title, desc, body, tags)
    create_article.expect_title_visible(title)

    create_article.page.screenshot(path="screenshots/article_created.png")
