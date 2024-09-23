import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.chrome(service=service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

