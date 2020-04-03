"""Driver factory for Selenium driver

This module is used to generate driver

Example:
    (TBD) Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.


"""
from selenium import webdriver
from appium import webdriver as webdriver_appium
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
 


class grid_driver_factory:
    """Only used for generating remote driver for selenium grid. remote driver could be customized 
    in case new features in orginal driver lib is not available

    Attributes:
        N/A

    """
    def create_driver(self, command_executor = 'http://10.128.224.24:4444/wd/hub', desired_capabilities:dict = None):
        """Generating remote driver.
        
            Args:
                desired_capabilities: - A dictionary of capabilities to request when
                 starting the browser session. Required parameter.
                 Web:
                    ANDROID = {'browserName': 'android', 'version': '', 'platform': 'ANDROID'}
                    CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
                    EDGE = {'browserName': 'MicrosoftEdge', 'version': '', 'platform': 'WINDOWS'}
                    FIREFOX = {'browserName': 'firefox', 'marionette': True, 'acceptInsecureCerts': True}
                    HTMLUNIT = {'browserName': 'htmlunit', 'version': '', 'platform': 'ANY'}
                    HTMLUNITWITHJS = {'browserName': 'htmlunit', 'version': 'firefox', 'platform': 'ANY', 'javascriptEnabled': True}
                    INTERNETEXPLORER = {'browserName': 'internet explorer', 'version': '', 'platform': 'WINDOWS'}
                    IPAD = {'browserName': 'iPad', 'version': '', 'platform': 'MAC'}
                    IPHONE = {'browserName': 'iPhone', 'version': '', 'platform': 'MAC'}
                    OPERA = {'browserName': 'opera', 'version': '', 'platform': 'ANY'}
                    PHANTOMJS = {'browserName': 'phantomjs', 'version': '', 'platform': 'ANY', 'javascriptEnabled': True}
                    SAFARI = {'browserName': 'safari', 'version': '', 'platform': 'MAC'}
                    WEBKITGTK = {'browserName': 'MiniBrowser', 'version': '', 'platform': 'ANY'}
                Android App:
                    ...               
                IOS App:
                    ...               
                Mac App:
                    ...                
                Windows App:
                    ...
                command_executor: - Either a string representing URL of the remote server or a custom
                 remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.

            Returns:
                remote driver.
    
        """
        CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        desired_capabilities = CHROME
        platform = desired_capabilities.get('platform')
        browserName= desired_capabilities.get('browserName', '')
#         if  automation_name == '':
        if platform == 'ANDROID' or  platform == 'IOS':
            logger.info('Creating driver for non Web app: '+platform)
            BuiltIn().log_to_console('Open Browser: '+str(desired_capabilities)+','+command_executor)
            driver = webdriver_appium.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)
            return driver
        else:
            if browserName is None:
                logger.info('Creating driver for non Web app: '+platform)
                BuiltIn().log_to_console('Open Browser: '+str(desired_capabilities)+','+command_executor)
                driver = webdriver_appium.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)
                return driver
            else:
                logger.info('Creating driver for non Web app: '+platform)
                BuiltIn().log_to_console('Open Browser: '+str(desired_capabilities)+','+command_executor)
                driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)
                return driver
            