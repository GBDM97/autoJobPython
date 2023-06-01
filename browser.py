from selenium import webdriver

def driver():
    chrome_driver_path = 'C:/Users/VAIO i7/Downloads/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    return driver