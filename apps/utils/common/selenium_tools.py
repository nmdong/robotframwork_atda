'''
Created on Apr 3, 2020

@author: nmdong
'''
import sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from builtins import len

class selenium_tools(object):
    '''
    classdocs
    '''
    #Set text to a element
    def setText(self, driver, by, value, text):
        try:
            print("<action>Setting text %s to: %s...", text, value)
            element = driver.find_element(by, value)
            element.clear()
            element.send_keys(text)
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("setText Failed" + '\n\n\n')
        
    def getText(self, driver, by, value):
        try:
            element = driver.find_element(by, value)
            print("Current text: " + str(element.gettext()))
            return element.gettext()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("setText getText" + '\n\n\n')
        return None
    
    def getElement(self, driver, elements, atIndex):
        try:
            return None
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("getElement getText" + '\n\n\n')
        return None
    
    # Get attribute value of element located by given locator.
    def getAttribute(self, driver, by, value, attribute):
        try:
            print("<action>Getting attribute's value: %s", attribute)
            return driver.find_element(by, value).getAttribute(attribute)
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("setText getText" + '\n\n\n')
        return None
    
    #Checking if element exists
    def isElement(self, driver, byLocator, value):
        try:
            print("<action>Checking if element exists %s", value)
            elements = driver.find_elements(byLocator, value)
            if len(elements) > 0:
                return True
            print("Not found elements")
        except:
            print("isElement Failed")
        return False
    
    def click(self, driver, by, value):
        try:
            print("<action>Click on elemnts")
            driver.find_element(by, value).click()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    def click_target_offset(self, driver, by, value, xoffset, yoffset):
        try:
            print("<action>Click on elemnts")
            # move and click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
            actions.click().perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    def click_if_exists(self, driver, by, value):
        try:
            print("<action>Click on elemnts if exists")
            if self.isElement(driver, by, value):
                driver.find_element(by, value).click()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    #Double click on element located by given locator.
    def double_click(self, driver, by, value):
        try:
            print("<action>Click on elemnts")
            # move and click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.double_click(element).perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    def double_click_target_offset(self, driver, by, value, xoffset, yoffset):
        try:
            print("<action>double_click on elemnts")
            # move and double_click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
            actions.double_click().perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    #Right click on element located by given locator.
    def right_click(self, driver, by, value):
        try:
            print("<action>Right clicking on elemnts")
            # move and click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.context_click(element).perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    def right_click_target_offset(self, driver, by, value, xoffset=None, yoffset=None):
        try:
            print("<action>double_click on elemnts")
            # move and double_click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
            actions.context_click().perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    #Mouse hover to element located by given locator.=No
    def mouse_hover(self, driver, by, value, xoffset=None, yoffset=None):
        try:
            print("<action>double_click on elemnts")
            # move and double_click the mouse like a user
            actions = ActionChains(driver)
            element = driver.find_element(by, value)
            actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("mouse_hover Failed" + '\n\n\n')
    
    #Wait until element located by given locator is clickable.
#     public static void waitUntilElementClickable(WebDriver driver, By byLocator,
    def wait_until_element_clickable(self, driver, by, value, time_out):
        try:
            print("<action>Waiting for %s seconds ultil element %s clickable...")
            element = driver.find_element(by, value)
            wait = WebDriverWait(driver, time_out)
            wait.until(EC.element_to_be_clickable(element))
        except:
            print("waitUntilElementClickable - Failed - Exception occurs: " + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("wait_until_element_clickable failed" + '\n\n\n')
    
    #Wait until element located by given locator appear.
    def wait_for_element_appear(self, driver, byLocator, value, time_out=10):
        try:
            print("<action>Waiting for % until element appears...")
            while(time_out>0):
                time_out = time_out - 1
                time.sleep(1)
                login_txt_ele = driver.find_elements(By.CSS_SELECTOR, value) 
                if self.isElement(driver, byLocator, value):
                    return True
            print("Not found element")
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("wait_for_element_appear Failed" + '\n\n\n')
        return False
        
    