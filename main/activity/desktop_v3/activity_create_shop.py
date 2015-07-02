from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
from main.page.base import BasePage
from main.page.pe_login import *
from selenium.common.exceptions import WebDriverException,NoSuchElementException, TimeoutException


class createShopActivity():
	def goto_createshop_page(driver):
		create_shop = createshop (driver)
		create_shop.in_shop_info()