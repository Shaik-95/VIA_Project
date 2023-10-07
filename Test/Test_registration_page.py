from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Utilities.Base_class import BaseClass
from Utilities.excel_module import HomePageData
from POM.cabs_list_page import CabsDetails
from POM.click_on_bookcab import CabPage
from POM.one_way_trip_page import OneWayTrip
from POM.registration_page import RegistrationPage

class TestFour(BaseClass):

    def test_register(from_loc, to_loc, name, email, mobile, driver_):
        
        bp = RegistrationPage(driver_)
      
        bp.enter_name(name)
        bp.enter_email(email)
        bp.enter_mobile(mobile)
        bp.click_submit()

