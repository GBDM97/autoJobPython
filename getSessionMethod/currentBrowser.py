from selenium import webdriver

def driver():
    url = 'http://localhost:55655'
    session_id = '9fa31706468072ce25e9bd071fa52fdf'
    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.close()   # this prevents the dummy browser
    driver.session_id = session_id
    return driver