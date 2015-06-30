from selenium import webdriver
import unittest
import time
import urllib


elem_directory_category = {
        'cat_lvl_1' : "div.span12 div.box div.rel-category-wrapper div.row-fluid div.span10 div.row-fluid h2.fs-15 a", 
        'cat_lvl_2' : "/html/body/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/ul/li/a", 
        'cat_lvl_3' : "/html/body/div/div[2]/div/div[7]/div/div/div/div/div[2]/div/ul/li/ul/li/a"
}

chromedriver= "D:\Python34\Scripts\chromedriver"
self.driver = webdriver.Firefox()
self.driver.set_window_size(1920, 1080)
driver.get("https://www.tokopedia.com/p/buku");


