from unittest import TestCase
from src.question_extractor import QuestionExtractor
from src.question import Question

__author__ = 'thanakorn'



class TestQuestionExtractor(TestCase):

    def test_extract_package_question_normal(self):
        qe = QuestionExtractor()
        question = qe.extract('what is my current package')
        self.assertEqual('what', question.question)
        self.assertEqual('is', question.verb)
        self.assertEqual('current', question.adjective)
        self.assertEqual('package', question.information)

    def test_extract_package_question_sentence(self):
        qe = QuestionExtractor()
        question = qe.extract('i want to know my current package')
        self.assertEqual('i want', question.question)
        self.assertEqual('know', question.verb)
        self.assertEqual('current', question.adjective)
        self.assertEqual('package', question.information)

    def test_extract_long_question_word(self):
        qe = QuestionExtractor()
        question = qe.extract('how much money i have to pay this month')
        self.assertEqual('how much', question.question)
        self.assertEqual('pay', question.verb)
