from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MyInfoPage(BasePage):

    MYINFO_MENU = (By.XPATH, "//span[text()='My Info']")

    def open_my_info(self):
        self.click(self.MYINFO_MENU)

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Personal Details')]")
            )
        )

    def menu_exists(self, menu_name):

        elements = self.driver.find_elements(
            By.XPATH,
            f"//*[contains(normalize-space(),'{menu_name}')]"
        )

        print(f"{menu_name} Found = {len(elements)}")

        return len(elements) > 0