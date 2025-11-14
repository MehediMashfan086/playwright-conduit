from pages.settings_page import SettingsPage
from utils import logger

log = logger.get_logger()


def test_update_setings(page):
    settings_page = SettingsPage(page)
    settings_page.go_to_home()
    settings_page.navigate()
    settings_page.update_settings(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkY36XkesV2esKBb7ds9iQinTHYG9R8pOGqQ&s",
        "mehedi086",
        "Software QA Automation Engineer",
        "mehedi_test@gmail.com",
        "Pass@123",
    )
    settings_page.expect_settings_update_done()
    settings_page.page.screenshot(path="screenshots/expect_settings_update_done.png")
    log.info(".... Settings Update Completed Successfully ....")
