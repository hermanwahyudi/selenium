import time
import urllib

def get_page_load_time(driver, url):
    request = urllib.request.urlopen(url)
    timestart = time.clock()
    driver.get(url)
    timeend = time.clock()
    loadtime = timeend-timestart
    print (url + " is successfully accessed with response code " + str(request.getcode()) + " in " + str(loadtime) + " second")
