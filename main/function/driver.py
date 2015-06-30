import platform
from selenium import webdriver

def useDriver(my_driver=""):

    if my_driver == "phantomjs":
        try:
            if platform.system() == 'Windows':
                print ("Test Machine : " + platform.system())
                use_driver = webdriver.PhantomJS(executable_path='../main/lib/executable/phantomjs-1.9.8-windows/phantomjs.exe')
                return use_driver
            elif platform.system() == 'Linux':
                print ("Test Machine : " + platform.system())
                use_driver = webdriver.PhantomJS(executable_path='../main/lib/executable/phantomjs-1.9.8-linux-x86_64/bin/phantomjs')
                return use_driver
        except:
            print ("PhantomJS driver path not found either in Windows & Linux! Please Check! ")

    # elif my_driver == "firefox":
    #     use_driver = webdriver.Firefox()
    #     return use_driver
    # elif my_driver == "chrome":
    #     use_driver = webdriver.Chrome(executable_path="D:\Python34\Scripts\chromedriver")
    #     return use_driver
    # else:
    #     print ("Driver not exists! please check your driver function class.")