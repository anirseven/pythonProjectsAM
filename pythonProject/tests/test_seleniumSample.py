import pytest
from selenium import webdriver

import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep


def test_lambaste_todo_app():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://www.google.com/sheets/about/')
    chrome_driver.maximize_window()
    title = "Google Sheets: Online Spreadsheet Editor | Google Workspace"
    assert title == chrome_driver.title

    sleep(10)
    chrome_driver.close()
