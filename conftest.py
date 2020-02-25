import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="function")
def browser():
    # browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    grid_url = "http://127.0.0.1:4444/wd/hub"
    desired_caps = DesiredCapabilities.CHROME
    browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    yield browser
    browser.quit()
