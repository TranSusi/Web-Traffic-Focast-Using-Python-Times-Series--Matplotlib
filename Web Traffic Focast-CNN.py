import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mozilla.org"
title = "Internet for people"

@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try: 
        element = wait(driver, 10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    #always quit driver
    driver.quit()

def test_add():
    assert 2 + 4 == 6

def test_web_links(webFix):
    webFix.find_elements_by_link_text("Learn more").click()
    title= webFix.title
    assert "Firefox" in title

def test_web_links(webFix):
    links = webFix.find_elements_by_tag_name("a")
    for link in links:
        href = link.get_attribute("href")
    assert 'cnbc.com' in href or 'bbc.com' in href \
        or 'mozilla' in href or 'firefox' in href \
            or 'buzzfeed' in href or 'getpocket' in href \
                or 'thenextweb' in href 

def test_account_form(webFix):
    webFix.find_element_by_link_text("Get a Firefox Account").click()
    try:
        element = wait(webFix, 3).until(
            EC.presence_of_element((By.CLASS_NAME, 'email tooltip-below'))
        )
    except Exception as ex:
        print(ex)
    text_input = webFix.find_element_by_tag_name('input')
    text_input.send_keys('fjordsail@gmail.com')
    webFix.find_element_by_id('submit-btn').click()
    prefillEmail = 'none'
    try:
        prefillEmail = wait(webFix, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME,
             'prefillEmail'))
        )
    except Exception as ex:
        print(ex)
    assert 'fjordsail@gmail.com' in prefillEmail.text







