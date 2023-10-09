from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time;
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

username = config['credentials']['username']
password = config['credentials']['password']

# Set the path to the chromedriver executable
chromedriver_path = 'C:\Program Files (x86)\chromedriver.exe'

# Create a Service object
chrome_service = Service(chromedriver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=chrome_service)
actions = ActionChains(driver)

# Open a webpage
driver.get('https://www.twitch.tv/')

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-a-target, "login-button")]')))
login_button.click()

username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login-username" and @data-a-target="tw-input"]')))
password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password-input')))


username_field.send_keys(username)
password_field.send_keys(password)

time.sleep(4)

submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@data-a-target="passport-login-button"]')))

submit_button.click()


# Allows the page to load for 10 seconds and find the search bar
search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-a-target="tw-input"]')))

# Input string into the text field
search_bar.send_keys("[insert streamer name]")

time.sleep(3)


# Returns the enter key
search_bar.send_keys(Keys.RETURN)

try:
    xqc_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/[insert href]"]')))
    xqc_link.click()
    
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-a-target="follow-button"]')))
    time.sleep(3)
    element.click()
    
except:
    print("Can't find stream")

while True:
    time.sleep(5)















