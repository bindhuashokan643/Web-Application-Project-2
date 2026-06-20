from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClaimPage:

    # Locators
    claim_menu = (By.XPATH, "//span[text()='Claim']")
    assign_claim = (By.XPATH, "//a[text()='Assign Claim']")

    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")

    event_dropdown = (By.XPATH,"(//div[contains(@class,'oxd-select-text')])[1]")

    accommodation_option = (By.XPATH, "//span[text()='Accommodation']")

    currency_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")

    currency_option = (By.XPATH, "//span[text()='Indian Rupee']")

    create_button = (By.XPATH, "//button[@type='submit']")

    success_message = (By.XPATH, "//h6[contains(text(),'Edit Claim Request')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_claim_module(self):
        self.wait.until(
            EC.element_to_be_clickable(self.claim_menu)
        ).click()

    def click_assign_claim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.assign_claim)
        ).click()

    def enter_employee_name(self, emp_name):
        self.wait.until(
            EC.visibility_of_element_located(self.employee_name)
        ).send_keys(emp_name)

    def select_event(self):
        self.wait.until(
            EC.element_to_be_clickable(self.event_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.accommodation_option)
        ).click()

    def select_currency(self):
        self.wait.until(
            EC.element_to_be_clickable(self.currency_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.currency_option)
        ).click()

    def create_claim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def is_claim_created(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).is_displayed()