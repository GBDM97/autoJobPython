import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from browser import driver

browser = driver()
jobTitle = "developer"
wait = WebDriverWait(browser, 10)


def easyApplyService(jobTitle):
    jobTitle.replace(" ", "20%")
    browser.get('https://www.linkedin.com/jobs/search/?currentJobId=3604095219&f_AL=true&geoId=106057199&keywords='+ jobTitle +'&location=Brazil&refresh=true&sortBy=DD')
    # job_elements = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item")))
    elements = browser.find_elements('css selector', '.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item')
    for element in elements:
        element.click()
        time.sleep(1)
def login():
    browser.maximize_window()
    time.sleep(1)
    browser.get('https://linkedin.com')
    browser.get('https://linkedin.com')
    browser.refresh()
    time.sleep(1)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "session_key")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "session_password")))
    email_input.send_keys("*****")
    password_input.send_keys("****")
    password_input.send_keys(Keys.ENTER)

login()
easyApplyService(jobTitle)







