from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from Utilities.generic import SeleniumWrapper



book_a_cab_link = (By.XPATH, "//a[text()='Book a Cab']")
switch_to_window_link = (By.XPATH, "//a[text()='Book a Cab']")
popup_link = (By.XPATH, "//button[text()='Later']")
from_location_link = (By.XPATH, "//input[@id='Autocomplete1']")
select_from_location_link = (By.XPATH, "//span[text()='hennai']")
to_location_link = (By.XPATH, "//input[@id='Autocomplete2']")
select_to_location_link = (By.XPATH, "//span[text()='yderabad']")

calender_link = (By.XPATH, "//input[@id='tripDate']")
day_ = 28
month_ = 'November 2023'
calender_month_link = (By.XPATH, f"//h2[text()='{month_}']")
calender_day_link = (By.XPATH, f"//td[text()='{day_}']")
calender_sidearrow_link = (By.XPATH, "//span[@class='fc-icon fc-icon-right-single-arrow']")

on_search_link = (By.XPATH, "//button[text()='Search Cabs']")

cab_name = 'AHA Economy'
cab_text = 'AHA ECONOMY'
on_bookcab_link = (By.XPATH, f"//h6[text()='{cab_name}']/../../following-sibling::div/child::div/child::button[text()='Book Now']")
enter_name_link = (By.XPATH, "//input[@id='name']")
enter_email_link = (By.XPATH, "//input[@id='email-id']")
enter_mobile_link = (By.XPATH, "//input[@id='mobile']")
on_book_link = (By.XPATH, "//button[@type='submit']/child::small[text()='Inc. GST, Toll and Taxes']")



class BookingPage(SeleniumWrapper):

    def click_book_a_cab(self):
        self.click_on_element(book_a_cab_link)

    def switch_windows(self):
        s = self.driver.window_handles
        self.driver.switch_to.window(s[1])
        self.window_handles(switch_to_window_link)

    def popup_(self):    
        self.click_on_element(popup_link)

    def from_location(self):
        self.enter_text(from_location_link)

    def click_from_location(self):
        self.click_on_element(select_from_location_link)

    def to_location(self):
        self.enter_text(to_location_link)

    def click_to_location(self):
        self.click_on_element(select_to_location_link)

    def start_date(self):
        self.click_on_element(calender_link)

        for _ in range(24):
            try:
                self.click_on_element(calender_month_link)
                break
            except NoSuchElementException:
                self.click_on_element(calender_sidearrow_link)
                continue
        try:
            self.click_on_element(calender_day_link)
        except NoSuchElementException:
            print("Invalid Date for the given month")

    def drop_down(self):
        sel = self.driver.find_element(By.XPATH, "//select[@ng-model='selectedpickuptime']")
        time_ = '02:30 PM'
        select = Select(sel)
        select.select_by_visible_text(f'{time_}')

    def click_on_search(self):
        self.click_on_element(on_search_link)    

    def click_on_booknow(self):
        lists = self.driver.find_elements(By.XPATH, "//div[@class='rightSide']")
        for words in lists:
            if  cab_text in words.text:
                self.click_on_element(on_bookcab_link)
            else:
                raise NoSuchElementException("no match")

    def enter_name(self):
        self.enter_text(enter_name_link)

    def enter_email(self):
        self.enter_text(enter_email_link)

    def enter_mobile(self):
        self.enter_text(enter_mobile_link)
    
    def click_submit(self):
        self.click_on_element(on_book_link)




