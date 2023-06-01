from selenium import webdriver

def driver():
    url = 'http://localhost:60867'
    session_id = '77a302006c05de5bd73eadca32ca2495'
    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.close()   # this prevents the dummy browser
    driver.session_id = session_id
    return driver