from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.NAME,"username")
    PASSWORD = (By.NAME,"password")
    LOGIN_BTN = (By.XPATH,"//button[@type='submit']")
    ERROR_MSG = (By.XPATH,"//p[contains(@class,'oxd-alert-content-text')]")



    def login(self,user,pwd):

        self.enter_text(self.USERNAME,user)
        self.enter_text(self.PASSWORD,pwd)
        self.click(self.LOGIN_BTN)

        #Wait until dashboard appears

       # WebDriverWait(self.driver, 20).until(
         #   EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
       # )

    def login_fields_visible(self):

        return self.driver.find_element(
            *self.USERNAME
        ).is_displayed

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def is_username_visible(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        return element.is_displayed() and element.is_enabled()

    def is_password_visible(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)

        )
        return element.is_displayed() and element.is_enabled()