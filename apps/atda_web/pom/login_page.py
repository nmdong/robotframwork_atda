'''
Created on Mar 31, 2020

@author: nmdong
login page
'''
import time
import sys
from robot.api import logger
from selenium.webdriver.common.by import By
from utils.common.selenium_tools import selenium_tools

class login_page():
    '''this class will define all locators and function on Login Page'''
    
    def __init__(self):
        self.LOGIN_TXT = "h1.auth-header" #css selector
        self.USERNAME_TF = "input.username" #css selector
        self.PASSWORK_TF = "input.password.auth-input.form-control" #css selector
        self.LOGIN_BTN = "button.mb-4.auth-button.btn.btn-primary"
        
    def loading_login_page(self, driver):
        if selenium_tools().wait_for_element_appear(driver, By.CSS_SELECTOR, self.LOGIN_TXT):
            print("loading_login_page TRUE")
            return True
        else:
            raise AssertionError("loading_login_page Failed" + '\n\n\n')
            return False
    
    def input_user_name(self, driver, userName):
        user_name_tf = driver.find_element(By.CSS_SELECTOR, self.USERNAME_TF)
        user_name_tf.send_keys(userName)
        
    def input_password(self, driver, password):
        password_tf_ele = driver.find_element(By.CSS_SELECTOR, self.PASSWORK_TF)
        password_tf_ele.send_keys(password)
    
    def click_login_btn(self, driver):
        login_btn_ele = driver.find_element(By.CSS_SELECTOR, self.LOGIN_BTN)
        login_btn_ele.click()
        