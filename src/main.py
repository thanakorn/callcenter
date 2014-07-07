__author__ = 'thanakorn'

import thread
from recognizer import SpeechRecognizer
from database import DatabaseManager
from callcenter import Callcenter

if __name__ == '__main__':
    phone_number = raw_input('Please input your phone number : ')

    ### Init component ###
    db = DatabaseManager()
    customer = db.find_user_info(phone_number)
    callcenter = Callcenter(customer)

    if customer:
        # Init component
        recognizer = SpeechRecognizer()
        callcenter.recognizer = recognizer
        recognizer.attach(callcenter)
        # Start speech recognition thread
        print('... Start recognizer ...')
        thread.start_new_thread(recognizer.start())

