__author__ = 'thanakorn'

import thread
from subprocess import call
from recognizer import SpeechRecognizer
from database import DatabaseManager


class Callcenter(object):

    def __init__(self):
        self.recognizer = None

    def speak(self, text):
        call(['espeak', text, '-s 150'])

    def update(self):
        self.recognizer.stop()
        print('I heard  : ' + self.recognizer.get_final_result())
        self.recognizer.resume()

if __name__ == '__main__':
    print('... Start callcenter ...')
    phone_number = raw_input('Please input your phone number : ')

    # Init component
    callcenter = Callcenter()
    recognizer = SpeechRecognizer()
    callcenter.recognizer = recognizer
    recognizer.attach(callcenter)
    db = DatabaseManager()

    # Start speech recognition
    print('... Start recognizer ...')
    thread.start_new_thread(recognizer.start())
