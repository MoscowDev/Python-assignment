import unittest

from code_levelling import*


class test_code_levelling (unittest.TestCase):
	def test_that_function_even_numbers(self):

		expected = 8 
		actual = get_even_numbers(8)

		self.assertEqual(actual,expected)



	def test_that_function_extract_five_character_words(self):

		expected =  ["elephant"]
		actual = extract_five_characters( ['cat', 'elephant', 'tiger', 'lion'])

		self.assertEqual(actual,expected)


	def test_that_function_returns_numbers_greater_than_two(self):

		expected =  [(4, 'B')]
		actual = get_values_greater_than_two([(1, 'A'), (4, 'B'), (2, 'C')])

		self.assertEqual(actual,expected)


	def test_that_function_returns_numbers_divisible_by_3_and_5(self):

		expected =  [15,30,45]
		actual = get_numbers_divisibe_by_3_and_5(1,51)

		self.assertEqual(actual,expected)