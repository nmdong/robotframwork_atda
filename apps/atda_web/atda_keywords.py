'''
Created on Apr 2, 2020

@author: nmdong
This module is used for defining parent class for ATDA keywords.

ATDA is automation test data analytics system. It could be break down into lower level if 


'''

import time
import sys
import os
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from utils.grid_manager.selenium_driver import selenium_driver
from utils.grid_manager.grid_driver_factory import grid_driver_factory
from atda_web.pom.login_page import login_page
from atda_web.pom.dash_board_page import dash_board_page
from utils.common.selenium_tools import selenium_tools

class atda_keywords(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """ Containing driver and all basic funciton.s

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    
    def adf(self):
        print("ddd")

    def __init__(self, ip_devices=None):
        """Example of docstring on the __init__ method.
 
        Examples:
            N/A
 
        Args:
            desired_capabilities: - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
            command_executor: - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.
 
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        if not ip_devices:
            command_executor='http://127.0.0.1:4444/wd/hub'
        BuiltIn().log_to_console('Init ATDA')
        self.desired_capabilities = CHROME
        self.command_executor = command_executor
         
    def open_browser(self, url):
        """Launch web browser with ATDA server info
   
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
   
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
   
        Note:
            Do not include the `self` parameter in the ``Args`` section.
   
        Args:  
            url (str): Link to website
   
        """
#         BuiltIn().log_to_console('Launching browser: ' + self.desired_capabilities.get('browserName'),'')
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
     
    def close_browser(self):
        """Close web browser
  
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
  
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
  
        Note:
            Do not include the `self` parameter in the ``Args`` section.
  
        Args:  
            url (str): Link to website
  
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        self.driver.quit()
        print('*INFO:%d* close_browser successfully' % (time.time()*1000))
    
    def verify_login_user_atda(self):
        """verify login user
  
        The method may be login user.
        return: TRUE/FALSE
  
        ex: verify_login_user
        """
        print("Starting function")
        return False
    
    def verify_login_page(self):
        """verify login page
  
        The method may be checking login page.
        return: TRUE/FALSE
  
        ex: verify_login_page
        """
        print("start function login page")
        if login_page().loading_login_page(self.driver):
            print("verify_login_page Pass")
        else:
            raise AssertionError("verify_login_page Failed" + '\n\n\n')
        
    def login_user_page(self, userName, password):
        """login user
  
        The method may be login user.
        return: TRUE/FALSE
  
        ex: verify_login_page
        """
        print("Start function login user " + userName)
        login_page().input_user_name(self.driver, userName)
        login_page().input_password(self.driver, password)
        login_page().click_login_btn(self.driver)
        
    def verify_login_user(self):
        print("Start function veridy login user")
        if dash_board_page().loading_avatar_page(self.driver, 10):
            print("verify_login_user passed ")
        else:
            print("verify_login_user failed")