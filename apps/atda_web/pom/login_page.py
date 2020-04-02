'''
Created on Mar 31, 2020

@author: nmdong
login page
'''
from robot.api import logger

from selenium.webdriver.common.by import By

class login_page():
    '''this class will define all locators and function on Login Page'''
    
    def __init__(self):
        self.USERNAME_TF = "username"
        self.PASSWORD_TF = "password"
        self.LOGIN_BTN = "//button[@class='mb-4 auth-button btn btn-primary']"   
        self.PROJECT_TITLE ="//div[@class='project-header row']"
        self.CREATE_ACCOUNT_BTN ="//a[@href=/register']" 
        self.URL_TITLE_TXT = "React App"
        self.INVALID_USERNAME_TXT ="//div[@class='mb-3 input-group']//div[@class='help-block invalid-feedback']"
        self.INVALID_PASSWORD_TXT ="//div[@class='mb-4 input-group']//div[@class='help-block invalid-feedback']" 
        self.INVALID_USERNAME_PASSWORD_TXT ="//*[text()='Username or Password invalid']"   
  
    def input_username_login(self, driver, username):
        element = driver.find_element(By.NAME, self.USERNAME_TF)
        element.send_keys(username)
        logger.info("input username in login page successfully")
         
    def input_password_login(self, driver, password):
        element = driver.find_element(By.NAME, self.PASSWORD_TF)
        element.send_keys(password)
        logger.info("input password successfully")
         
    def click_login_button(self, driver):
        element = driver.find_element(By.XPATH, self.LOGIN_BTN)
        element.click()
        logger.info("click login button successfully")
    