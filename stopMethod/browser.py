from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def driver():
    chrome_driver_path = 'C:/Users/VAIO i7/Downloads/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.maximize_window()
    driver.execute_script("alert('Login manually');")
    cont = input("press anything to continue")
    return driver
