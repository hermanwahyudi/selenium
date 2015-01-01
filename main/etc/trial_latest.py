import unittest
import time
import datetime
import urllib
from urllib.error import HTTPError
from function.get_report import *
from selenium import webdriver
import requests

list_cat = []
list_product =[]
list_product_img =[]

now = datetime.datetime.now()




elem_directory_category = {
        'cat_lvl_1' : "div.span12 div.box div.rel-category-wrapper div.row-fluid div.span10 div.row-fluid h2.fs-15 a", 
        'cat_lvl_2' : "/html/body/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/ul/li/a", 
        'cat_lvl_3' : "/html/body/div/div[2]/div/div[7]/div/div/div/div/div[2]/div/ul/li/ul/li/a"
}



class TestSweepProduct(unittest.TestCase):
    
    def setUp(self):
        chromedriver= "D:\Python34\Scripts\chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.set_window_size(1920, 1080)

    #Fungsi check image product di kategori
    """"def test_check_img_product_in_cat(self):
        driver = self.driver
        
        def check_directory_list(driver):
            driver.get("https://test.tokopedia.nginx/p")
            
            print ("START SCANNING DIRECTORY LIST...")
            print ("================================")
            for cat_lvl_1 in driver.find_elements_by_css_selector(elem_directory_category['cat_lvl_1']):
                print (cat_lvl_1.get_attribute("href"))
                list_cat.append(cat_lvl_1.get_attribute("href"))
             
#            for cat_lvl_2 in driver.find_elements_by_xpath(elem_directory_category['cat_lvl_2']):
#                print (cat_lvl_2.get_attribute("href"))
#                list_cat.append(cat_lvl_2.get_attribute("href"))
#                
#            for cat_lvl_3 in driver.find_elements_by_xpath(elem_directory_category['cat_lvl_3']):
#                print (cat_lvl_3.get_attribute("href"))
#                list_cat.append(cat_lvl_3.get_attribute("href"))
             
            print ("TEST CHECKING DIREKTORI DIMULAI")
            check_img_product_in_cat(driver)
        
        
        def check_img_product_in_cat(driver):
            
            total_img_ok = 0
            total_img_modified = 0
            total_img_error_500 = 0
            total_img_error_404 = 0
            total_img_error_502 = 0
            total_img_error_504 = 0    
            total_img_error_others = 0
            
            for x in list_cat:
                driver.get(x)
                for b in driver.find_elements_by_xpath("//*[@id='content-directory']/div[1]/div/a/div/div[1]/img"):
                    print (b.get_attribute("src"))
                    list_product_img.append(b.get_attribute("src"))
                time.sleep(3)
                
                
            for y in list_product_img:
                request = urllib.request.urlopen(y)
                driver.get(y) #akses setiap gambar product di halaman direktori page 1
                time.sleep(0.5)
                #if request.getcode() == "200":
                #    print (y + " is successfully accessed (200 OK)")
                if request.getcode() == 200:
                    print (y + " is successfully accessed with response code " + str(request.getcode()))
                    total_img_ok += 1
                elif request.getcode()== 304:
                    print (y + " is successfully accessed with response code " + str(request.getcode()))
                    total_img_modified +=1
                elif request.getcode() == 404:
                    print (y + " got error with response code " + str(request.getcode()))
                    total_img_error_404 += 1
                elif request.getcode() == 504:
                    print (y + " got error with response code " + str(request.getcode()))
                    total_img_error_504 += 1
                elif request.getcode() == 502:
                    print (y + " got error with response code " + str(request.getcode()))
                    total_img_error_502 += 1
                elif request.getcode() == 500:
                    print (y + " got error with response code " + str(request.getcode()))
                    total_img_error_500 += 1
                #elif request.getcode() == "504":
                #  print(y + " is GATEWAY TIMEOUT 504")
                #  total_img_error_504 += 1
                else:
                    print (y + " error with response code " + str(request.getcode()))
                    total_img_error_others += 1
                
                
            print ("URL Image Result(OK 200) : %s" %(str(total_img_ok)))
            print ("URL Image Result(OK but Not modified 304) : %s" %(str(total_img_modified)))
            print ("URL Image Result(ERROR 404) : %s" %(str(total_img_error_404)))
            print ("URL Image Result(ERROR 500) : %s" %(str(total_img_error_500)))
            print ("URL Image Result(ERROR 502) : %s" %(str(total_img_error_502)))
            print ("URL Image Result(ERROR 504) : %s" %(str(total_img_error_504)))
            print ("URL Image Result(OTHER ERRORS) : %s" %(str(total_img_error_others)))
    
#=====Fungsi Check List Product======
    #    def check_product_in_cat(driver):
    #        for x in list_cat:
    #            driver.get(x)
    #            #for b in driver.find_elements_by_css_selector("div.main-content div#content-directory div.grid-shop-product div.product a"):
    #            #Check dan tampung link Product di halaman direktori 1
    #            for b in driver.find_elements_by_xpath("//*[@id='content-directory']/div[1]/div/a"):
    #                print (b.get_attribute("href"))
    #                list_product.append(b.get_attribute("href"))
    #            time.sleep(5)
    #        
    #        for y in list_product:
    #            driver.get(y) #akses setiap hal product di halaman direktori page 1
    #            time.sleep(3)
    
            
        check_directory_list(driver)"""


    def test_check_index_product_in_cat(self):
        driver = self.driver
        
        def check_directory_list(driver, report_dir_row):
            
            driver.get("https://test.tokopedia.nginx/p")
            requests.get('https://test.tokopedia.nginx', verify = True)

            print ("START SCANNING DIRECTORY LIST...")
            print ("================================")
            for cat_lvl_1 in driver.find_elements_by_css_selector(elem_directory_category['cat_lvl_1']):
                print (cat_lvl_1.get_attribute("href"))
                list_cat.append(cat_lvl_1.get_attribute("href"))
                report_dir_sheet.write(report_dir_row,  report_dir_col,  cat_lvl_1.get_attribute("href"))
                report_dir_row += 1
                
#            for cat_lvl_2 in driver.find_elements_by_xpath(elem_directory_category['cat_lvl_2']):
#                print (cat_lvl_2.get_attribute("href"))
#                list_cat.append(cat_lvl_2.get_attribute("href"))
#                report_dir_sheet.write(report_dir_row,  report_dir_col,  cat_lvl_2.get_attribute("href"))
#                report_dir_row += 1
#    
#                    
#            for cat_lvl_3 in driver.find_elements_by_xpath(elem_directory_category['cat_lvl_3']):
#                print (cat_lvl_3.get_attribute("href"))
#                list_cat.append(cat_lvl_3.get_attribute("href"))
#                report_dir_sheet.write(report_dir_row,  report_dir_col,  cat_lvl_3.get_attribute("href"))
#                report_dir_row += 1

            
            report_dir.close()
            
            
            print ("TEST CHECKING DIREKTORI DIMULAI")
            check_product_in_cat(driver, report_index_product_row)
        
        def check_product_in_cat(driver, report_index_product_row):
            
            total_product_ok = 0
            total_product_modified = 0
            total_product_error_500 = 0
            total_product_error_404 = 0
            total_product_error_502 = 0
            total_product_error_504 = 0    
            total_product_error_others = 0
            
            for dir in list_cat:
                driver.get(dir)
                
                #while True:
                    
                try:
                    for each_product in driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div/div/div[1]/div/a"):
                        print (each_product.get_attribute("href"))
                        list_product.append(each_product.get_attribute("href"))
                    time.sleep(3)
                        #break
                        
                        #Fungsi untuk check "next page"
#                        next_page = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[last()]/a")
#                        if next_page.text == "»" :
#                            page_numb = page_numb +1
#                            print("masuk ke halaman %s" %str(page_numb))
#                            print (next_page.text)
#                            
#                            driver.get(next_page.get_attribute("href"))
#                            
#                            time.sleep(5)
#                        else :
#                            break
                except:
                    print ("No product / catalog")
                    report_index_product_sheet.write(report_index_product_row, report_index_product_col, dir)
                    report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, "No Product/Catalog")
                    report_index_product_row += 1
                        
                    
#                    if next_page.is_displayed != True:
#                        break
                
            
    
            for product in list_product:
                
                try:
                    request = urllib.request.urlopen(product)                    
                    driver.get(product) #akses setiap gambar product di halaman direktori page 1
                    load_time = requests.get(product).elapsed.total_seconds()
                    time.sleep(0.5)
                    if request.code == 200:
                        print (product + " is successfully accessed with response code " + str(request.getcode()) + " in " + str(load_time) + " second")
                        print (request.getcode())
                        total_product_ok += 1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write('C1', "Load Time (Second)", bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(request.getcode()))
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+2, str(load_time))
                        report_index_product_row += 1
                except HTTPError as err:
                    print ("Response code error : %s"  %err.code)
                    if err.code==404:
                        print (product + " got error with response code " + str(err.code))
                        total_product_error_404 +=1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(err.code))
                        report_index_product_row += 1
                    elif err.code==500:
                        print (product + " got error with response code " + str(err.code))
                        total_product_error_500 += 1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(request.getcode()))
                        report_index_product_row += 1
                    elif err.code == 504:
                        print (product + " got error with response code " + str(err.code))
                        total_product_error_504 += 1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(err.code))
                        report_index_product_row += 1
                    elif err.code == 502:
                        print (product + " got error with response code " + str(err.code))
                        total_product_error_502 += 1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(err.code))
                        report_index_product_row += 1
                    else:
                        print (product + " error with response code " + str(err.code))
                        total_product_error_others += 1
                        report_index_product_sheet.write('A1',"Product Link", bold)
                        report_index_product_sheet.write('B1',"Status Code",  bold)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col, product)
                        report_index_product_sheet.write(report_index_product_row, report_index_product_col+1, str(err.code))   
                        report_index_product_row +=1


                                                        
                
            print ("URL Index Product Result(OK 200) : %s" %(str(total_product_ok)))
            print ("URL Index Product Result(OK but Not modified 304) : %s" %(str(total_product_modified)))
            print ("URL Index Product Result(ERROR 404) : %s" %(str(total_product_error_404)))
            print ("URL Index Product Result(ERROR 500) : %s" %(str(total_product_error_500)))
            print ("URL Index Product Result(ERROR 502) : %s" %(str(total_product_error_502)))
            print ("URL Index Product Result(ERROR 504) : %s" %(str(total_product_error_504)))
            print ("URL Index Product Result(OTHER ERRORS) : %s" %(str(total_product_error_others)))
            
            report_index_product.close()
        
        check_directory_list(driver, report_dir_row)
    
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()

""""while (1) :
    for member in list_cat :
        driver.get(member)
        time.sleep(3)"""
                
