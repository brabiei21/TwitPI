# install: selenium, webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

## options for driver/browser ##
opts = Options()
# opts.add_argument("--headless")               # uncomment to run as headless
opts.add_argument("start-maximized")          # starts browser maximized

## webdriver/browser with defined options/settings ##
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
driver.implicitly_wait(15) # will wait up to 15 seconds for things to load when grabbing elements

DEFAULT_URL = "https://twitter.com/"    # default url **do NOT change!**
page = "mojang"                         # twitter user's profile page

## go to webpage ##
driver.get(DEFAULT_URL+page)

driver.close()


