from time import sleep
from selenium import webdriver

# Initialize firefox and load instagram
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

# Load user info from file
with open('.uinfo', 'r') as infile:
    username = infile.readline().strip()
    password = infile.readline().strip()

# Login
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Bypass 'Save Your Login Info' screen
next_button = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
next_button.click()

# Bypass 'Turn on Notifications' popup
next_button = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
next_button.click()

# sleep(5)
# browser.close()