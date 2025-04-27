import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_find_parent_and_first_child(driver):
    driver.get("https://www.guvi.in/")
    assert driver.title == 'GUVI | Learn to code in your native language'

def test_find_second_sibling(driver):
    driver.get("https://www.guvi.in/")
    assert driver.current_url == 'https://www.guvi.in/'


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_parent_of_href(driver):
    driver.get("https://www.guvi.in/")



