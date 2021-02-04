from selenium import webdriver
from config.readConfig import *
import os


# chrome启动参数设置
def driver_config():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    download_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))+'\\materials')
    prefs = {'download.default_directory': download_path}
    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(desired_capabilities=caps, chrome_options=options)
    return browser
