from selenium.webdriver.common.by import By

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from Utilities.generic import SeleniumWrapper


class CabsDetails(SeleniumWrapper):
    cab_name = 'AHA Economy'
    cab_text = 'AHA ECONOMY'
    on_book_cab_link = (By.XPATH, f"//h6[text()='{cab_name}']/../../following-sibling::div/child::div/child::button[text()='Book Now']")
    
    def __init__(self, driver):
        self.driver = driver

    def click_on_booknow(self):

        lists = self.driver.find_elements(By.XPATH, "//div[@class='rightSide']")
        for words in lists:
            if  CabsDetails.cab_text in words.text:
                self.click_on_element(CabsDetails.on_book_cab_link)
            else:
                raise NoSuchElementException("no match")