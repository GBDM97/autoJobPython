import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from browser import driver

browser = driver()
wait = WebDriverWait(browser, 10)
actions = ActionChains(browser)

def easyApplyService():
    browser.get('https://www.linkedin.com/jobs/search/?currentJobId=3515371199&f_AL=true&geoId=106057199&keywords=developer&location=Brazil&refresh=true&sortBy=DD')
    # job_elements = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item")))
    elements = browser.find_elements('css selector', '.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item')
    for element in elements:
        element.click()
        time.sleep(1)
        actions.move_by_offset(700, 430).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.ID, "ember543"))).click()

def login():
    browser.maximize_window()
    time.sleep(1)
    browser.get('https://linkedin.com')
    browser.get('https://linkedin.com')
    browser.refresh()
    time.sleep(1)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "session_key")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "session_password")))
    email_input.send_keys("***")
    password_input.send_keys("***")
    password_input.send_keys(Keys.ENTER)

easyApplyService()







