from playwright.sync_api import sync_playwright
from login_page import LoginPage
import unittest


class TableCheckTest(unittest.TestCase):

    def test_login(self):
        """
        Test login with invalid credentials.
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            login_page = LoginPage(page)
            login_page.goto_login_page()
            login_page.login('test@.com', 'test123')
            assert login_page.is_login_failed()

            browser.close()


if __name__ == "__main__":

    unittest.main()
