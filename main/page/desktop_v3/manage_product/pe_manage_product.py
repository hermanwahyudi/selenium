from main.page.base import *
from selenium.webdriver.common.by import By

class ManageProduct(BasePage):
    #manage product locators
    _combobox_product_loc = (By.CSS_SELECTOR, "a.selectBox.mr-5.mb-0.select-custom-all-product.filter-select." +
                                             "selectBox-dropdown.selectBox-menuShowing.selectBox-menuShowing-bottom")
    _combobox_category_loc = (By.CSS_SELECTOR, "a.selectBox.mr-5.mb-0.select-custom-catalog.filter-select.selectBox-dropdown.selectBox-menuShowing.selectBox-menuShowing-bottom")
    _combobox_catalog_loc = (By.CSS_SELECTOR, "a.selectBox.mr-5.mb-0.select-custom-catalog.filter-select.selectBox" +
                                             "-dropdown.selectBox-menuShowing.selectBox-menuShowing-bottom")
    _combobox_image_loc = (By.CSS_SELECTOR, "a.selectBox.mr-5.mb-0.select-custom-image.filter-select.selectBox-" +
                                            "dropdown")
    _combobox_conditions_loc = (By.CSS_SELECTOR, "a.selectBox.mr-5.mb-0.select-custom-condition.filter-select." +
                                                 "selectBox-dropdown")
    _search_key_loc = (By.CSS_SELECTOR, "")
    _combobox_position_loc = (By.CSS_SELECTOR, "")
    _checkbox_curr_loc = (By.CSS_SELECTOR, "")
    _textbox_curr_loc = (By.CSS_SELECTOR, "")

    #main
    _combobox_setting_loc = (By.CSS_SELECTOR, "")
    _button_set_loc = (By.CSS_SELECTOR, "")
    _checkbox_product_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[1]/" +
                                       "input")
    _pro_name_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[2]/a")
    _pro_curr_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[3]/form/div/" +
                               "select")
    _pro_price_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[3]/form/div/" +
                                "input[1]")
    _add_wholesale_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[3]/form/" +
                                    "small/a")
    _pro_edit_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/p/small/" +
                               "a[1]")
    _pro_copy_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/p/small/" +
                               "a[2]")
    _move_numb_one_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[4]/div/div/table/tbody/tr[2]/td[5]/p/" +
                                    "small/a[3]") #you must hover first to show this button
    _20_per_page_loc = (By.CSS_SELECTOR, "")
    _40_per_page_loc = (By.CSS_SELECTOR, "")
    _60_per_page_loc = (By.CSS_SELECTOR, "")