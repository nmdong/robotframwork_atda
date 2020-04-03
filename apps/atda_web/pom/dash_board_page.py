'''
Created on Apr 3, 2020

@author: nmdong
'''
import time
from selenium.webdriver.common.by import By

class dash_board_page(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.AVATAR = "img.img-avatar"
        
    def loading_avatar_page(self, driver, timeOut):
        avartar_ele = driver.find_elements(By.CSS_SELECTOR, self.AVATAR)        
        i = timeOut
        while i > 10:
            time.sleep(1)
            i = i+1
            if avartar_ele.size() > 0:
                print("loading_avatar_page TRUE")
                return True
            else:
                print("Not fount elemnets")
        return False