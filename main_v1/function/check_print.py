import time
import datetime



def check_print(driver, cur_page):    
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if driver.current_url == cur_page:
    
        print ("["+cur_time+"]" + " Berhasil masuk di Halaman " + driver.current_url)
    else :
        print ("["+cur_time+"]" + " Gagal masuk ke halaman %s tetapi masuk ke %s" %(cur_page , driver.current_url))
    time.sleep(4)
