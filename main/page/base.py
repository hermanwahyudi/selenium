import time, requests, os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from main.function.general import wait_visible_element, timestamp_print, timestamp_print_verify_url
from urllib.error import HTTPError
from requests import exceptions

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _open(self, url):
        url = self.url
        self.get_page_load_time(url)
        #fungsi bawaan yang gw belom cukup level untuk pemakaian-nya.
        #assert self.on_page(), 'Did not land on %s' % url

    def get_page_load_time(self, url): #Fungsi untuk mengakses suatu halaman dan waktu proses-nya
        #response = urllib.request.urlopen(url)

        try:
            timestart = time.clock()
            self.driver.get(url)
            response = requests.head(url)
            timeend = time.clock()
            loadtime = timeend-timestart

            timestamp_print(self.url, loadtime)
        except TimeoutException:
            print ("Timeout terlalu lama, melebihi 300s")
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
        timestamp_print_verify_url(self.driver.current_url, loadtime)
        #print (self.driver.current_url + " is accessed in " + str(loadtime) + " second")

    def check_visible_element(self, by, element):
        retry = 0

        while(retry<3):
            try:
                wait_visible_element(self.driver, by, element)
                break
            except NoSuchElementException:
                retry += 1
                print ("Load Element is taking too long.. retry attempt %s" %(retry))
                self.driver.refresh()

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
        return self.driver.find_elements(*loc)

    def on_page(self):
        return self.driver.current_url == (self.url)








