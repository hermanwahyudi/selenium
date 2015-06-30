import time,datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException,NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


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

#Fungsi wait_visible_element yg dipakai dibawah ini
def wait_visible_element(driver, by, element):
    try:
        WebDriverWait(driver,15).until(EC.presence_of_element_located((by, element)))
    except NoSuchElementException:
        no_element = print ("Element not found! skip.")
        return no_element
    except TimeoutException:
        timeout = print ("Timeout! skip.")
        return timeout


#Fungsi basic untuk print log
def timestamp_print(url, loadtime, log_data):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print ("["+current_time+"] " + url + " is accessed in " + str('{0:.3g}'.format(loadtime)) + " second")
    log_add = "["+current_time+"] " + url + " is accessed in " + str('{0:.3g}'.format(loadtime)) + " second"
    log_data += str(log_add)
    #log_to_file(log_data)


def timestamp_print_verify_url(url, loadtime, log_data):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print ("["+current_time+"] " + url + " is accessed by click in "+ str('{0:.3g}'.format(loadtime)) + " second")
    log_add = "["+current_time+"] " + url + " is accessed by click in "+ str('{0:.3g}'.format(loadtime)) + " second"
    log_data += str(log_add)
    #log_to_file(log_data)

def log_to_file(var):
    # log_flag = None
    # if log_flag == 1:
    with open("coba.txt", "a") as text_file:
         print (var, file=text_file)

