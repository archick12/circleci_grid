import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import socket

@pytest.fixture(scope="function")
def browser():
   # browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
   host_name = socket.gethostname()
   host_ip = socket.gethostbyname(host_name)
   grid_url = "http://" + host_ip +":4444/wd/hub"
   desired_caps = DesiredCapabilities.CHROME
   browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
   yield browser
   browser.quit()
