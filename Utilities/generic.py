from Utilities.wait_module import wait_
from selenium.common.exceptions import *


class SeleniumWrapper:

	def __init__(self, driver):
		self.driver = driver
	#   def click_on_element(self, locator_type, locator_value):
	# 	driver.find_element(locator_type, locator_value).click()

	@wait_          # click_on_element = wait_(click_on_element)
	def click_on_element(self, locator):
		self.driver.find_element(*locator).click()

	@wait_
	def enter_text(self, locator, *, value):
		self.driver.find_element(*locator).send_keys(value)

	@wait_   
	def window_handles(self, locator):
		self.driver.find_element(*locator).click()

