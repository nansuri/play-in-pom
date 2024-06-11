from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home_page(self):
        self.page.goto('https://www.tablecheck.com/en/join/')

    def is_sign_in_button_visible(self):
        return self.page.is_visible('text="Sign In"')
