__author__ = 'thanakorn'

import thread
from recognizer import SpeechRecognizer
from database import DatabaseManager
from callcenter import Callcenter

if __name__ == '__main__':
    phone_number = raw_input('Please input your phone number : ')

    # Init component
    db = DatabaseManager()
    callcenter = Callcenter()
    recognizer = SpeechRecognizer()
    callcenter.recognizer = recognizer
    recognizer.attach(callcenter)

    # Retrieve customer information
    customer = db.find_user_info(phone_number)
    if customer:
        # Greeting message
        callcenter.greeting(customer)

        # Start speech recognition thread
        print('... Start recognizer ...')
        thread.start_new_thread(recognizer.start())

    else:
        callcenter.speak('Sorry, we cannot find your phone number.')
