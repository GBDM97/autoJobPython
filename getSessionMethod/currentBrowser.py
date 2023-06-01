from selenium import webdriver

def driver():
    url = 'http://localhost:57885'
    session_id = '050a2f237d013eb7c23f79ac5db6323a'
    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.close()   # this prevents the dummy browser
    driver.session_id = session_id
    return driver