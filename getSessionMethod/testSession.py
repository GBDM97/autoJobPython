from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException

# Provide the session ID
session_id = "a6165b6becfc1c8f20ae557de89be0ec"

# Create a dummy WebDriver instance
driver = webdriver.Remote(command_executor='https://127.0.0.1:54330/devtools/browser/06a923ac-29f9-4796-a496-bc4884fdc779')
driver.session_id = session_id

try:
    # Perform a simple action to check the validity of the session ID
    driver.current_url
    print("Session ID is valid")

except InvalidSessionIdException:
    print("Invalid session ID")

# Close the driver when done
driver.quit()
