from selenium.webdriver.common.by import By

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from Utilities.generic import SeleniumWrapper


class CabPage(SeleniumWrapper):

    book_a_cab_link = (By.XPATH, "//a[text()='Book a Cab']")

    def __init__(self, driver):
        self.driver = driver

    def click_book_a_cab(self):
        return self.click_on_element(CabPage.book_a_cab_link)

    def switch_windows(self):
        s = self.driver.window_handles
        self.driver.switch_to.window(s[1])
        self.window_handles(CabPage.switch_to_window_link)

