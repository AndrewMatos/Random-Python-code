import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""

	def setUp(self):
		"""Create an instace of a survey and set of response for use in all test methods """
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['english', 'spanish', 'latin']


	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three respones are stored properly """
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()