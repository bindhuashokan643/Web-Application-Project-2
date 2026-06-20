from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    menu_items = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard"
    ]

    def verify_menu_items(self):

        # Wait for dashboard page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            )
        )

        for item in self.menu_items:

            menu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//span[text()='{item}']")
                )
            )

            assert menu.is_displayed()

            print(f"{item} menu is visible")
