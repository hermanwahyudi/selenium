
#this one is imported for mobile
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#this one is not used for mobile
import time, requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.function.general import wait_visible_element, timestamp_print, timestamp_print_verify_url
from utils.lib.user import Environment
from urllib.error import HTTPError
from requests import exceptions

class PageBaseMobile(object):

    def __init__(self, driver):
        self.driver = driver

    def explicit_wait(self, locator):
        return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, locator)))

    def swipeLeft(self):
        self.driver.swipe(100,835,900,835,150)

    def swipeRight(self):
        self.driver.swipe(900,835,100,835,150)

    def swipeUp (self):
        self.driver.swipe(250,150,250,800,300)

    def swipeDown(self, startx=250, starty=800, endx=250, endy=150, dur=300):
        self.driver.swipe(startx, starty, endx, endy, dur)

    def snooze(self, x=2):
        sleep(x)

    def get_page_load_time(self, url): #Fungsi untuk mengakses suatu halaman dan waktu proses-nya
        #response = urllib.request.urlopen(url)
        retry = 0
        set_time_out = 60
        while (retry<3):
            try:
                timestart = time.clock()
                self.driver.set_page_load_timeout(set_time_out)
                self.driver.get(url)

                if "www" in url :
                    response = requests.get(url, verify = True)
                elif "dev" or "nginx" or "beta" in url:
                    response = requests.get(url, verify = False)
                timeend = time.clock()
                loadtime = timeend-timestart

                timestamp_print(url, loadtime, self.log_result)
                break

            except TimeoutException:
                print ("Load Page takes too long, it's over %s second" %(set_time_out))
                self.driver.refresh()
                retry +=1
            except requests.exceptions.HTTPError:
                if response.status_code == 500:
                    print ("Error code 500 : Maaf, saat ini Tokopedia sedang kepenuhan pengunjung. ")
                elif response.status_code == 503:
                    print ("Error code 503 : Tokopedia sedang maintenance.")
                elif response.status_code == 502:
                    print ("Error code 502 : Bad Gateway.")
                elif response.status_code ==504:
                    print ("Error code 504 : Gateway Timeout.")


    def _click(self, loc):
        timestart = time.clock()
        loc.click()
        timeend = time.clock()
        loadtime = timeend-timestart
        timestamp_print_verify_url(self.driver.current_url, loadtime, self.log_result)
        #print (self.driver.current_url + " is accessed in " + str(loadtime) + " second")

    def check_visible_element(self, by, element):
        retry = 0

        while(retry<3):
            try:
                WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((by,element)))
                break
            except NoSuchElementException:
                retry += 1
                print ("Element not found.. retry attempt %s" %(retry))
            except TimeoutException:
                retry +=1
                print ("Load Element is taking too long.. retry attempt %s" %(retry))

    def check_clickable_element(self, by, element):
        retry = 0

        while(retry<3):
            try:
                WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((by,element)))
                break
            except NoSuchElementException:
                retry += 1
                print ("Element not found.. retry attempt %s" %(retry))
            except TimeoutException:
                retry +=1
                print ("Load Element is taking too long.. retry attempt %s" %(retry))


    def click_on_javascript(self, target_element):
        self.mouse = webdriver.ActionChains(self.driver)
        return self.mouse.move_to_element(target_element).click().perform()

    def mouse_hover_to(self, by, element):
        target_element = self.find_element(by, element)
        self.check_visible_element(by, element)
        hover_to_target = ActionChains(self.driver).move_to_element(target_element)
        hover_to_target.perform()
        return target_element


    #Find single element
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    #Find multiple element
    def find_elements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            print(" ")

    def on_page(self):
        return self.driver.current_url == (self.url)


class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

#Return value based on the value of an input from class object
def case(*args):
    return any((arg == switch.value for arg in args))








