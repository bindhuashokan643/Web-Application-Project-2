import pytest
import time

from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from utilities.config import BASE_URL


@pytest.mark.regression
def test_tc08_validate_myinfo_menu(driver):

    # Open OrangeHRM
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)

    login.login("Admin", "admin123")
    print("Login Successful")

    # Open My Info
    myinfo = MyInfoPage(driver)

    myinfo.open_my_info()

    time.sleep(3)

    expected_menus = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary",
        "Report-to",
        "Qualifications",
        "Memberships"
    ]

    print("\n===== MY INFO MENU VALIDATION =====")

    for menu in expected_menus:

        print(f"\nChecking : {menu}")

        assert myinfo.menu_exists(menu), f"{menu} Not Found"

        print(f"{menu} is Present")

    print("\nAll My Info Menu Items Validated Successfully")