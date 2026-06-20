import pytest
from pages.login_page import LoginPage
from pages.claim_page import ClaimPage
from utilities.config import BASE_URL


@pytest.mark.claim
def test_tc10_claim_request(driver):

    login = LoginPage(driver)
    claim = ClaimPage(driver)

    # Login
    driver.get(BASE_URL)

    login.login("Admin", "admin123")


    print("Login Successful")

    # Claim Module
    claim.open_claim_module()
    print("Claim Module Opened")

    claim.click_assign_claim()


    claim.enter_employee_name("Pooja")

    claim.select_event()

    claim.select_currency()

    claim.create_claim()
    current_url = driver.current_url
    assert "assignClaim" in current_url
    print("Claim Request Submitted")

    assert claim.is_claim_created()

    print("Claim Request Created Successfully")