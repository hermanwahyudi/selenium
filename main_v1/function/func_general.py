import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
import sys


'TOP BAR'
elem_topBar_css = {
        'registerLink' : "div.pull-right ul.topbar-nav li.dropdown-single a",
        'loginLink' : "div.pull-right ul.topbar-nav li.dropdown-right a"
    }

elem_leftPanel ={
        'depositLink' : "div#side-profile div.clear-b div.span8 div.ellipsis a"
                                
}

def ajax_wait(driver):
    try:
        return 0 == driver.execute_script("return JQuery.active")
    except WebDriverException:
        pass

def wait_visible_then_click(element,browser):
    element = WebDriverWait(browser,5,poll_frequency=.2).until(EC.visibility_of(element))
    element.click()
    time.sleep(5)
    
def driver_wait(driver):
    wait = ui.WebDriverWait(driver, 20)
    return wait
    
    
    
def WaitForElement(webdriver, path):
    limit = 5   # waiting limit in seconds
    inc = 0.5   # in seconds; sleep for 500ms
    c = 0
    while (c < limit):
        try:
            print ("Waiting... " + str(c))
            yes = webdriver.find_element_by_xpath(path)
            print (yes + " Found!")
            return 1
        except:
            time.sleep(inc)
            c = c + inc 
 
    print (sys.exc_info())
    print ("The element hasn't been found.")
    return 0

