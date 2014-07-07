__author__ = 'thanakorn'

from recognizer import SpeechRecognizer
from subprocess import call
from question import Question
from question_extractor import QuestionExtractor
from response_generator import ResponseGenerator
from voice import speak
import time

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
        text = text.split('.')
        for t in text:
            if len(t) > 0:
                print('phrase : ' + t)
                speak(t)
                time.sleep(3)
            #if len(speak_text) + len(t) < 100:
            #    speak_text += (t + ' ')
            #else:
            #    speak(speak_text)
            #    speak_text = t
            #    time.sleep(10)
        #speak(speak_text)
        #call(['espeak', text, '-s 120'])

    def update(self):
        self.recognizer.stop()
        # Callcenter processing
        qe = QuestionExtractor()
        response = ResponseGenerator()
        question = qe.extract(self.recognizer.get_final_result())
        self.speak(response.generate_response_message(question, self.user))
        self.recognizer.resume()