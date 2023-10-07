from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Utilities.Base_class import BaseClass
from Utilities.excel_module import HomePageData


from POM.cabs_list_page import CabsDetails
from POM.click_on_bookcab import CabPage
from POM.one_way_trip_page import OneWayTrip
from POM.registration_page import RegistrationPage

class TestThree(BaseClass):

    def test_list(from_loc, to_loc, name, email, mobile, driver_):
        
        bp = CabsDetails(driver_)
        
        bp.click_on_booknow()


