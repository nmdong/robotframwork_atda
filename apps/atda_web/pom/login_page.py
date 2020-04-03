'''
Created on Mar 31, 2020

@author: nmdong
login page
'''
import time
from robot.api import logger
from selenium.webdriver.common.by import By

class login_page():
    '''this class will define all locators and function on Login Page'''
    
    def __init__(self):
        self.LOGIN_TXT = "h1.auth-header" #css selector
        self.USERNAME_TF = "input.username" #css selector
        self.PASSWORK_TF = "input.password.auth-input.form-control" #css selector
        self.LOGIN_BTN = "button.mb-4.auth-button.btn.btn-primary"
        
    def loading_login_page(self, driver):
        login_txt_ele = driver.find_elements(By.CSS_SELECTOR, self.LOGIN_TXT)        
        i = 0
        while i > 10:
            time.sleep(1)
            i = i+1
            if login_txt_ele.size() > 0:
                print("loading_login_page TRUE")
                return True
            else:
                print("Not fount elemnets")
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