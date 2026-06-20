from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:

    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    ADD_USER_HEADER = (By.XPATH, "//h6[text()='Add User']")
    SEARCH_USERNAME = (By.XPATH, "//input[contains(@class,'oxd-input')])[2]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESULT_TABLE = (By.XPATH, "//div[@role='table']")


    def __init__(self, driver):
        self.driver = driver

    def create_user(self):
        print("Step 1: Click Admin")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADMIN_MENU)
        ).click()

        print("Step 2: Click Add")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

        print("Step 3: Waiting for Add User page")

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ADD_USER_HEADER)
        )

        print("Step 4: Add User page opened")

    def search_user(self, username):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADMIN_MENU)
        ).click()

        print("Admin Menu Opened")

        search_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.SEARCH_USERNAME)
        )

        search_box.clear()
        search_box.send_keys(username)

        print("Username Entered")

        self.driver.find_element(*self.SEARCH_BUTTON).click()

        print("Search Button Clicked")