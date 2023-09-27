import pytest
from Project_VIA.POM.booking_page import BookingPage
from Project_VIA.Utilities.config import Config



data = [ ]


@pytest.mark.parametrize("fname, lname, email, pwd, confirm_pwd", data)
def test_register(fname, lname, email, pwd, confirm_pwd, driver_):
    try:
        bp = BookingPage(driver_)
        bp.book_a_cab_link(driver_)
        bp.switch_to_window_link()
        bp.popup_link()
        bp.from_location_link()
        bp.select_from_location_link()
        bp.to_location_link()
        bp.select_to_location_link()
        bp.calender_link()
        bp.calender_month_link()
        bp.calender_day_link()
        bp.calender_sidearrow_link()
        bp.on_search_link()
        bp.on_bookcab_link()
        bp.enter_name_link()
        bp.enter_email_link()
        bp.enter_mobile_link()
        bp.on_book_link()
		
    except Exception as msg:
        from datetime import datetime
        td = datetime.now()

        driver_.save_screenshot(Config.SCREENSHOT_PATH + f"screenshot1-{td.day}-{td.second}.png")
        raise msg
	

