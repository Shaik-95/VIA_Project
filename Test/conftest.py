import pytest
from selenium import webdriver
from Utilities.config import Config


@pytest.fixture(params=["chrome", "edge"])
def driver_(request):
	browser = request.param
	
	if browser == "chrome":
		opts = webdriver.ChromeOptions()
		opts.add_experimental_option("detach", True)
		driver = webdriver.Chrome(options=opts)

	elif browser == "edge":
		opts = webdriver.EdgeOptions()
		opts.add_experimental_option("detach", True)
		driver = webdriver.Edge(options=opts)

	driver.get("https://in.via.com/cab-bookings")
	driver.maximize_window()
	yield driver
	driver.quit()
