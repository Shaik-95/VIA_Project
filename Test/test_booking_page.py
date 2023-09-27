import pytest
from POM.booking_page import BookingPage
from Utilities.config import Config
from Utilities.excel_module import read_excel


@pytest.mark.parametrize("from_loc, to_loc, name, email, mobile", read_excel())
def test_register(from_loc, to_loc, name, email, mobile, driver_):
    try:
        bp = BookingPage(driver_)
        bp.click_book_a_cab()
        bp.switch_windows()
        bp.popup_()
        bp.from_location(from_loc)
        bp.click_from_location()
        bp.to_location(to_loc)
        bp.click_to_location()
        bp.start_date()
        bp.drop_down()
        bp.click_on_search()
        bp.click_on_booknow()
        bp.enter_name(name)
        bp.enter_email(email)
        bp.enter_mobile(mobile)
        bp.click_submit()

    except Exception as msg:
        from datetime import datetime
        td = datetime.now()

        driver_.save_screenshot(Config.SCREENSHOT_PATH + f"screenshot1-{td.day}-{td.second}.png")
        raise msg
