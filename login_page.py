from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_login_page(self):
        self.page.goto('https://app.tablecheck.com/')

    def enter_email(self, email):
        self.page.fill('input[id="email"]', email)

    def enter_password(self, password):
        self.page.fill('input[id="password"]', password)

    def click_login_button(self):
        self.page.click('button[type="submit"]')

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def is_login_failed(self):
        invalid_indicator = '//*[@id="root"]/div/div[1]/div[3]/form/div[1]'

        return self.page.wait_for_selector(invalid_indicator)
