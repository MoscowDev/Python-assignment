
import unittest

from main_logistics_Services import *


class test_main_logistics_Services(unittest.TestCase):
	def test_that_sender_logistics_function_returns_correct_value_less_than_50_percent(self):

		expected = 9800 
		actual = get_drivers_payment_per_day(30)

		self.assertEqual(actual,expected)



	def test_that_sender_logistics_function_returns_correct_value_greater_than_50_percent_and_less_than_60_percent(self):

		expected = 16000 
		actual = get_drivers_payment_per_day(55)
		self.assertEqual(actual,expected)


	def test_that_sender_logistics_function_returns_correct_value_greater_than_or_equal_60_percent_and_less_than_70_percent(self):

		expected = 22000 
		actual = get_drivers_payment_per_day(68)
		self.assertEqual(actual,expected)


	def test_that_sender_logistics_function_returns_correct_value_greater_than_or_equal_70_percent(self):

		expected = 43500 
		actual = get_drivers_payment_per_day(77)
		self.assertEqual(actual,expected)

	def test_that_sender_logistics_function_collects_the_correct_type(self):

		anything = "chelsea"
		self.assertRaises(TypeError, anything)

		excess = 3.000
		self.assertRaises(TypeError,excess)

	#def test_that_sender_logistics_function_handles_negative_value(self):

		#self.assertRaises(ValueError,get_drivers_payment_per_day, -1)

