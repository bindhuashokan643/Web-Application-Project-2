from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FORGOT_LINK = (By.XPATH, "//p[contains(@class,'orangehrm-login-forgot-header')]")

    USERNAME = (By.NAME, "username")

    RESET_BUTTON = (By.XPATH, "//button[@type='submit']")

    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'orangehrm-forgot-password-title')]")

    def click_forgot_password(self):
        self.click(self.FORGOT_LINK)

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def click_reset(self):
        self.click(self.RESET_BUTTON)


    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)