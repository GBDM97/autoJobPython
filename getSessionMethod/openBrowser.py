from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = 'C:/Users/VAIO i7/Downloads/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.execute_script("alert('Login manually please, to continue run apply with the session id');")
session_id = driver.session_id
url = driver.command_executor._url
print(f"Session ID ================>>>>>>>  {session_id}")
print(f"URL ================>>>>>>>  {url}")
