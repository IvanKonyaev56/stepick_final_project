from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# language = "en"
options.add_experimental_option('prefs', {'intl.accept_languages': "en-US, en"})
browser = webdriver.Chrome(options=options)