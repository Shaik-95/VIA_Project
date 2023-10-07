from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Utilities.Base_class import BaseClass
from Utilities.excel_module import HomePageData
from POM.cabs_list_page import CabsDetails
from POM.click_on_bookcab import CabPage
from POM.one_way_trip_page import OneWayTrip
from POM.registration_page import RegistrationPage

class TestTwo(BaseClass):

    def test_oneway(from_loc, to_loc, name, email, mobile, driver_):
        
        bp = OneWayTrip(driver_)
        
        bp.popup_()
        bp.from_location(from_loc)
        bp.click_from_location()
        bp.to_location(to_loc)
        bp.click_to_location()
        bp.start_date()
        bp.drop_down()
        bp.click_on_search()
        
