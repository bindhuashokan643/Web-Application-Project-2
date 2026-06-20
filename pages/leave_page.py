from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeavePage(BasePage):

    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    ASSIGN_LEAVE = (By.XPATH, "//a[text()='Assign Leave']")

    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    LEAVE_TYPE = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")

    FROM_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    TO_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")

    ASSIGN_BUTTON = (By.XPATH, "//button[@type='submit']")

    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")

    def open_assign_leave(self):
        self.click(self.LEAVE_MENU)
        self.click(self.ASSIGN_LEAVE)

    def enter_employee(self, employee):
        self.enter_text(self.EMPLOYEE_NAME, employee)

    def select_leave_type(self):
        self.click(self.LEAVE_TYPE)

    def enter_from_date(self, date):
        self.enter_text(self.FROM_DATE, date)

    def enter_to_date(self, date):
        self.enter_text(self.TO_DATE, date)

    def click_assign(self):
        self.click(self.ASSIGN_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)