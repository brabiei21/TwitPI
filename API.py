from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

## path to chrome browser relative to file project ##
CHROMIUM_PATH = "Win_Chrome\chrome-win\chrome-win\chrome.exe"

## options for driver/browser ##
opts = Options()
# opts.add_argument("--headless")               # uncomment to run as headless
opts.add_argument("--window-size=1920x1080")    # size of browser

## webdriver/browser with defined options/settings ##
driver = webdriver.Chrome(chrome_options=opts, executable_path=CHROMIUM_PATH)


driver.get("https://google.com")