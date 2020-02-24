import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="function")
def browser():
    # browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    print("ENVIRONMENT VARIABLES " + os.environ)
    grid_url = "http://" + os.environ['TEST_IP_ADDRESS'] + ":4444/wd/hub"
    grid_url = "http://" + os.environ['TEST_IP_ADDRESS'] + ":4444/wd/hub"
    desired_caps = DesiredCapabilities.CHROME
    browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    yield browser
    browser.quit()
