__author__ = 'thanakorn'

import thread
from subprocess import call
from recognizer import SpeechRecognizer


class Callcenter(object):

    def __init__(self):
        self.recognizer = None

    def speak(self, text):
        call(['espeak', text, '-s 150'])

    def update(self):
        print('I heard  : ' + self.recognizer.get_final_result())

if __name__ == '__main__':
    print('Start callcenter')
    callcenter = Callcenter()
    recognizer = SpeechRecognizer()
    callcenter.recognizer = recognizer
    recognizer.attach(callcenter)
    print('Start recognizer')
    thread.start_new_thread(recognizer.start(None),())
