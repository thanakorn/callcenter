__author__ = 'thanakorn'

from recognizer import SpeechRecognizer
from subprocess import call


class Callcenter(object):

    def __init__(self):
        self.recognizer = None

    @staticmethod
    def speak(text):
        call(['espeak', text, '-s 120'])

    def greeting(self, user):
        greeting_message = 'good morning %s %s %s. how can i help you,' % ('mister' if user['gender'] == 'male' else 'miss', user['firstname'], user['lastname'])
        self.speak(greeting_message)

    def update(self):
        self.recognizer.stop()
        # Do something
        self.recognizer.resume()