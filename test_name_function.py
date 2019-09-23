import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
	""" Tests for 'name function.py'. """
	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work? """
		formatted_name = get_formated_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		""" Do names like ' Wolfgang Amadeus Mozart' work? """
		formatted_name = get_formated_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__' :
	unittest.main()