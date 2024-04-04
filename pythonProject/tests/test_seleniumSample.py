import pytest
from selenium import webdriver

import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep


def test_lambaste_todo_app():
    server = 'http://localhost:4444'
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Remote(command_executor=server, options=options)
    #chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://www.google.com/sheets/about/')
    chrome_driver.maximize_window()
    title = "Google Sheets: Online Spreadsheet Editor | Google Workspace"
    assert title == chrome_driver.title
    print(chrome_driver.title)

    sleep(10)
    chrome_driver.close()
