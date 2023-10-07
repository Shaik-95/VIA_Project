from selenium.webdriver.common.by import By

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from Utilities.generic import SeleniumWrapper


class OneWayTrip(SeleniumWrapper):

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
    
    def __init__(self, driver):
        self.driver = driver

    def popup_(self):
        return self.click_on_element(OneWayTrip.popup_link)

    def from_location(self, from_loc):
        return self.enter_text(OneWayTrip.from_location_link)

    def click_from_location(self):
        return self.click_on_element(OneWayTrip.select_from_location_link)

    def to_location(self, to_loc):
        return self.enter_text(OneWayTrip.to_location_link)

    def click_to_location(self):
        return self.click_on_element(OneWayTrip.select_to_location_link)

    def start_date(self):

        self.click_on_element(OneWayTrip.calender_link)

        for _ in range(24):
            try:
                self.click_on_element(OneWayTrip.calender_month_link)
                break
            except NoSuchElementException:
                self.click_on_element(OneWayTrip.calender_sidearrow_link)
                continue
        try:
            self.click_on_element(OneWayTrip.calender_day_link)
        except NoSuchElementException:
            print("Invalid Date for the given month")

    def drop_down(self):
        sel = self.driver.find_element(By.XPATH, "//select[@ng-model='selectedpickuptime']")
        time_ = '02:30 PM'
        select = Select(sel)
        select.select_by_visible_text(f'{time_}')
        
    
    def click_on_search(self):
        return self.click_on_element(OneWayTrip.on_search_link)  