from selenium.webdriver.common.by import By

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from Utilities.generic import SeleniumWrapper


class RegistrationPage(SeleniumWrapper):

    enter_name_link = (By.XPATH, "//input[@id='name']")
    enter_email_link = (By.XPATH, "//input[@id='email-id']")
    enter_mobile_link = (By.XPATH, "//input[@id='mobile']")
    on_book_link = (By.XPATH, "//button[@type='submit']/child::small[text()='Inc. GST, Toll and Taxes']")
    
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        return self.enter_text(RegistrationPage.enter_name_link)

    def enter_email(self, email):
        return self.enter_text(RegistrationPage.enter_email_link)

    def enter_mobile(self, mobile):
        return self.enter_text(RegistrationPage.enter_mobile_link)
    
    def click_submit(self):
        return self.click_on_element(RegistrationPage.on_book_link)

