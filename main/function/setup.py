import random
from random import randint
from main.function.driver import *

def tsetup(my_driver=""):
    if platform.system() == 'Windows':
        print ("Platform : windows")
        a= randint(1,2)
        if my_driver == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif my_driver == "chrome":
            driver = webdriver.Chrome(executable_path="../main/lib/executable/chromedriver")
            return driver
        elif my_driver == "phantomjs":
            driver = webdriver.PhantomJS(executable_path='../main/lib/executable/phantomjs-1.9.8-windows/phantomjs.exe')
            return driver
        elif a == 1:
            driver = webdriver.Firefox()
            return driver
        elif a == 2:
            driver = webdriver.Chrome(executable_path="../main/lib/executable/chromedriver")
            return driver

    elif platform.system() == 'Linux':
        driver = useDriver("phantomjs")
        return driver