import time, requests, os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from main.function.general import wait_visible_element, timestamp_print, timestamp_print_verify_url
from urllib.error import HTTPError
from requests import exceptions

class BasePage(object):
    log_result = ""
    url = ""
    site = {
        "live-site" : "https://www.tokopedia.com/",
        "beta-site" : "https://beta.tokopedia.com/",
        "test-site" : "https://test.tokopedia.nginx/",
        "dev-site" : "https://www.tokopedia.dev/"
    }

    def __init__(self, driver):
        self.driver = driver

    def _open(self, site="", pl=""):
        if(site == "dev"):
            self.url = self.site['dev-site']
        elif(site == "nginx"):
            self.url = self.site['test-site']
        elif(site == "beta"):
            self.url = self.site['beta-site']
        elif(site == "live"):
            self.url = self.site['live-site']
        else:
            self.url = site

        self.get_page_load_time(self.url + pl)
        #fungsi bawaan yang gw belom cukup level untuk pemakaian-nya.
        #assert self.on_page(), 'Did not land on %s' % url

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
                elif "nginx" or "beta" in url:
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








