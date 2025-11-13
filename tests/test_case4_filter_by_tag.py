from pages.filter_page import FilterPage


def test_filter_articles_by_tag(page):
    filter_page = FilterPage(page)

    filter_page.go_to_home()
    tag_text = filter_page.select_random_tag()
    filter_page.verify_feed_for_tag(tag_text)
    filter_page.verify_articles_loaded()
    filter_page.take_screenshot(tag_text)

    print(".... TEST COMPLETED SUCCESSFULLY ....")
