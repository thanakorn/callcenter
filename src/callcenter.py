__author__ = 'thanakorn'

from recognizer import SpeechRecognizer
from subprocess import call
from question import Question
from question_extractor import QuestionExtractor
from response_generator import ResponseGenerator


class Callcenter(object):

    def __init__(self, user):
        self.recognizer = None
        self.user = user
        if user:
            greeting_message = 'good morning %s %s %s. How can i help you?' % ('mister' if self.user['gender'] == 'male' else 'miss', self.user['firstname'], self.user['lastname'])
        else:
            greeting_message = 'sorry, we cannot find your phone number.'
        self.speak(greeting_message)

    @staticmethod
    def speak(text):
        call(['espeak', text, '-s 120'])

    def update(self):
        self.recognizer.stop()
        # Callcenter processing
        qe = QuestionExtractor()
        response = ResponseGenerator()
        question = qe.extract(self.recognizer.get_final_result())
        self.speak(response.generate_response_message(question, self.user))
        self.recognizer.resume()