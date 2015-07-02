import platform, os
from selenium import webdriver

def useDriver(my_driver=""):
    latest_phantom =  "/home/selenium/phantomjs-2.0.0/bin/phantomjs"
    legacy_phantom = "../../../utils/lib/executable/phantomjs-1.9.8-linux-x86_64/bin/phantomjs"
    retry = 0


    if my_driver == "phantomjs":
        #latest_phantom =  "../../../utils/lib/executable/phantomjs-2.0.0/bin/phantomjs"
        while retry < 3:
            try:
                if platform.system() == 'Windows':
                    print ("Test Machine : " + platform.system())
                    use_driver = webdriver.PhantomJS(executable_path='../../../utils/lib/executable/phantomjs-2.0.0-windows/bin/phantomjs')
                    return use_driver
                elif platform.system() == 'Linux':
                    print ("Test Machine : " + platform.system())
                    #use_driver = webdriver.PhantomJS(executable_path='../../../utils/lib/executable/phantomjs-1.9.8-linux-x86_64/bin/phantomjs')
                    if os.path.exists(latest_phantom):
                        use_driver = webdriver.PhantomJS(executable_path=latest_phantom,service_args=['--load-images=no'])
                        print ("sukses ke phantom 2.0.0")
                        return use_driver
                    elif os.path.exists(legacy_phantom):
                        use_driver = webdriver.PhantomJS(executable_path=legacy_phantom,service_args=['--load-images=no'])
                        print ("sukses ke phantom 1.9.8")
                        return use_driver
                    else:
                        print ("Latest and Legacy Phantom Path not found!")
            except:
                retry += 1
                print ("PhantomJS driver path not found either in Windows & Linux! Please Check!")
                print ("Retry attempt : %s" %(retry))

