from utilities.config import BASE_URL


def test_testcase_02(driver):

    driver.get(BASE_URL)

    assert "orangehrmlive.com" in driver.current_url