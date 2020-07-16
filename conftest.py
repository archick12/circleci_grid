import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from testrail_api import TestRailAPI


# @pytest.fixture(scope="function")
# def browser():
    # grid_url = "http://127.0.0.1:4444/wd/hub"
    # desired_caps = DesiredCapabilities.CHROME
    # browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    # yield browser
    # browser.quit()





@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    test_run_id = 1
    test_rail_url = "https://piluck.testrail.io"
    test_rail_user_name = "a.a.piluck@gmail.com"
    test_rail_api_key = "rusiiS8CqY9hVuaH/sM2-ylp5Z2rSieshDNcGS1zw"
    test_rail_status_id = 0
    test_rail_comment = ""

    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("test_case")
    api = TestRailAPI(test_rail_url, test_rail_user_name, test_rail_api_key)
    if marker.name == "test_case":
    # if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            test_rail_status_id = 5
            test_rail_comment = "Failed"
        elif rep.when == "call" and rep.passed:
            test_rail_status_id = 1
            test_rail_comment = "PASSED"
        if rep.when != "setup":
            result = api.results.add_result_for_case(
                run_id=test_run_id,
                case_id=marker.kwargs["parameters"]["id"],
                status_id=test_rail_status_id,
                comment=test_rail_comment,
                version="1"
            )


