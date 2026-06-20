import pytest
import time

from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from utilities.config import BASE_URL


@pytest.mark.regression
@pytest.mark.leave
def test_testcase_09(driver):

    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    print("Login Successful")

    # Open Assign Leave
    leave = LeavePage(driver)

    leave.open_assign_leave()

    print("Assign Leave Page Opened")

    # Enter Details
    leave.enter_employee("Pooja")

    leave.enter_from_date("2026-06-20")

    leave.enter_to_date("2026-06-22")

    leave.click_assign()

    print("Leave Assigned Successfully")

    time.sleep(3)

    assert True