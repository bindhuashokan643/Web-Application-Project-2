import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.config import BASE_URL


@pytest.mark.smoke
def test_verify_menu_items(driver):

    # Open Application
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    # Verify Menu Items
    dashboard = DashboardPage(driver)
    dashboard.verify_menu_items()

    print("All menu items are visible and functional")