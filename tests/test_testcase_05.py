import pytest
import random
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utilities.config import BASE_URL


@pytest.mark.smoke
def test_testcase_05(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    # Login as Admin
    login.login("Admin", "admin123")
    print("After Login URL =", driver.current_url)
    print("Page Title =", driver.title)

    admin = AdminPage(driver)
    admin.create_user()
    print("Current URL:", driver.current_url)
    print("New user login successful")