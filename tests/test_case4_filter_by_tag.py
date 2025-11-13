import random

from playwright.sync_api import expect


def test_filter_articles_by_tag(page):
    page.goto("https://conduit.bondaracademy.com/")
    expect(page.locator("a:has-text('New Article')")).to_be_visible(timeout=8000)
    print("Logged in successfully using saved session")

    page.wait_for_selector(".tag-list a", timeout=10000)

    tags = page.locator(".tag-list a")
    tag_count = tags.count()
    assert tag_count > 0, "No tags found in sidebar"

    random_index = random.randint(0, tag_count - 1)
    tag_text = tags.nth(random_index).inner_text().strip()
    print(f"Selected random tag: {tag_text}")

    tags.nth(random_index).click()

    selected_feed = page.locator(".feed-toggle li.nav-item a.active")

    actual_text = selected_feed.inner_text().strip()
    assert (
        tag_text.lower() in actual_text.lower()
    ), f"Expected active feed to include tag '{tag_text}', but got '{actual_text}'"

    print(f"Filter applied for tag: {actual_text}")

    articles = page.locator(".article-preview")
    expect(articles.first).to_be_visible(timeout=10000)
    print("Articles loaded successfully under selected tag")

    page.screenshot(path=f"screenshots/filter_by_tag_{tag_text}.png")
    print(f"Screenshot captured for tag '{tag_text}'")

    print(".... TEST COMPLETED SUCCESSFULLY ....")
