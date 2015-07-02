import random, os
import time,sys
from random import randint
from appium import webdriver as AWD
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from utils.function.driver import *

def tsetup(my_driver=""):
    if platform.system() == 'Windows':
        print ("Platform : windows")
        a= randint(1,2)
        if my_driver == "firefox":
            FF_profile = FirefoxProfile()
            FF_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')  #--Disable Flashplayer
            FF_profile.set_preference('permissions.default.stylesheet', 2)
            FF_profile.set_preference('permissions.default.image',2)  #--Disable Image
            driver = webdriver.Firefox(firefox_profile=FF_profile)  #-- initiate Firefox driver using profiler
            return driver
        elif my_driver == "chrome":
            driver = webdriver.Chrome(executable_path="../../../utils/lib/executable/chromedriver")
            return driver
        elif my_driver == "phantomjs":
            #Latest phantomdriver update : 27/2/2015
            driver = webdriver.PhantomJS(executable_path='../../../utils/lib/executable/phantomjs-1.9.8-windows/phantomjs', service_args=['--load-images=no']) #--Disable Image
            return driver
        elif a == 1:
            driver = webdriver.Firefox()
            return driver
        elif a == 2:
            driver = webdriver.Chrome(executable_path="../../../utils/lib/executable/chromedriver")
            return driver

    elif platform.system() == 'Linux':
        driver = useDriver("phantomjs")
        return driver

def tsetup_andr(driver=""):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    
    # Returns abs path relative to this file and not cwd
    # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'../apps/Tokopedia.apk'))
    desired_caps['appPackage'] = 'com.tokopedia.tkpd'
    desired_caps['appActivity'] = '.SplashScreen'
    driver = AWD.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.reset()
    return driver

def ctimer(elapsed_time):
    count = elapsed_time
    while count > 0:
        if count > 0:
            time.sleep(1)
            print("%s..." %(count))
            count -=1
        if count < 1:
            break
    else:
        print ("Timer got an error!")
