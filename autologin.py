# Python module to handle time-related tasks
import time

# import WebDriver class
from selenium import webdriver

# import Service class
# manages the starting and stopping of the ChromeDriver
from selenium.webdriver.chrome.service import Service

# import By class
# set of supported locator strategies which lets us identify elements in the DOM
from selenium.webdriver.common.by import By

#import login credentials file 
import creds

# define a Browser class
class Browser:
  
    # initialise browser and service to null
    browser, service = None, None
    
    # constructor for a Browser object
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
        
    # function to navigate to page url
    def open_page(self, url: str):
        self.browser.get(url)
        
    # function to close the browser
    def close_browser(self):
        self.browser.close()
        
    Automatically log into iZone (or any website) using Python & Selenium 4
    # function to type content into a field specified by arguments
    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)
        
    # function to click on buttons specified by arguments
    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)
        
    # function to login into iZone
    # can be used to login into any sites, modify as needed
    # pass in corresponding IDs for username, password fields and submit button
    def login_izone(self, username: str, password: str):
        self.add_input(by=By.ID, value='student_uid', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.ID, value='submit')
        
# driver code
if __name__ == '__main__':
    browser = Browser('drivers/chromedriver')
    browser.open_page('https://izone.sunway.edu.my/login')
    browser.login_izone(creds.username, creds.password)
