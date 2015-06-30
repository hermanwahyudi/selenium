from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib

chromedriver= "D:\Python34\Scripts\chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1920, 1080)

driver.get ("https://www.tokopedia.com/p")

list_cat = []
list_product =[]
list_product_img =[]

def check_img_in_product(driver):
    total_img_ok = 0
    total_img_error = 0
    for x in list_cat:
        driver.get(x)
        for b in driver.find_elements_by_xpath("//*[@id='content-directory']/div[1]/div/a/div/div[1]/img"):
            print (b.get_attribute("src"))
            list_product_img.append(b.get_attribute("src"))
        time.sleep(3)
        
    for y in list_product_img[1:2]:
        request = urllib.request.urlopen(y)
        driver.get(y) #akses setiap gambar product di halaman direktori page 1
        time.sleep(0.5)
        total_img_ok += 1
        if request.getcode() == "404":
            print (y + "PAGE NOT FOUND 404")
            total_img_error += 1
        
            
        """"if driver.assertEqual(request.getcode(), 200) == True:
            print (y + "diakses dengan status code 200")
        else :
            print ("test aja")"""
    print ("URL Image Result(OK) : %s" %(str(total_img_ok)))
    print ("URL Image Result(ERROR) : %s" %(str(total_img_error)))

def check_product_in_cat(driver):
    for x in list_cat[1:4]:
        driver.get(x)
        #for b in driver.find_elements_by_css_selector("div.main-content div#content-directory div.grid-shop-product div.product a"):
        #Check dan tampung link Product di halaman direktori 1
        for b in driver.find_elements_by_xpath("//*[@id='content-directory']/div[1]/div/a"):
            print (b.get_attribute("href"))
            list_product.append(b.get_attribute("href"))
        time.sleep(5)
    
    for y in list_product:
        
        driver.get(y) #akses setiap hal product di halaman direktori page 1
        time.sleep(4)
        
            
        

for a in driver.find_elements_by_css_selector("div.span12 div.box div.rel-category-wrapper div.row-fluid div.span10 div.row-fluid h2.fs-15 a"):
    print (a.get_attribute("href"))
    list_cat.append(a.get_attribute("href"))
    
print ("test checking direktori dimulai")
check_img_in_product(driver)


""""while (1) :
    for member in list_cat :
        driver.get(member)
        time.sleep(3)"""
                
