__author__ = 'thanakorn'

from database import DatabaseManager
from question import Question


class ResponseGenerator(object):

    def __init__(self):
        self._db = DatabaseManager()

    def generate_response_message(self, question, customer):
        if question.information == 'package':
            package = self._db.find_user_package(customer['phone_number'])
            # Recommend package
            if question.verb in ['know', 'recommend', 'have'] and question.adjective in ['internet', 'calling', 'calling and internet']:
                recommend_packages = self._db.find_package_by_category(question.adjective, package['payment'])
                response = 'we recommend %d packages for you. ' % (recommend_packages.count())
                for p in recommend_packages:
                    response += '%s. ' % (p['name'])
                    if package['payment'] == 'postpaid':
                        response += 'maximum calling time is %d minutes, maximum speed internet data is %d gigabytes and monthly fee is %d baht. ' % (p['calling_time'], p['max_speed_data'], p['fee'])
                    elif package['payment'] == 'prepaid':
                        response += 'internal calling rate is %.2f baht per minute, external calling rate is %.2f baht per minute, and registration fee is %d baht. ' % (p['internal_calling_rate'], p['external_calling_rate'], p['registration_fee'])
                return response
            # Ask for current package
            elif question.question in ['what', 'which'] and (question.adjective is None or question.adjective == 'current'):
                if package['payment'] == 'postpaid':
                    response = 'your current package is %s. maximum call time is %d minutes. maximum internet speed data is %d gigabytes. monthly fee is equal to %d baht.' % (package['name'], package['calling_time'], package['max_speed_data'], package['fee'])
                else:
                    response = 'your current package is %s. internal calling rate is %.2f baht per minute. external calling rate is %.2f baht per minute. registration fee is %d baht.' % (package['name'], package['internal_calling_rate'], package['external_calling_rate'], package['registration_fee'])
                return response
            # Otherwise
            else:
                return 'sorry i do not understand your question'

        elif question.information in ['bill', 'money', 'balance', 'account']:
            # Get user's package
            package = self._db.find_user_package(customer['phone_number'])
            if question.question == 'how much':
                if package['payment'] == 'postpaid':
                    bill = self._db.find_latest_bill(customer)
                    addition_calling_time = 0 if bill['calling_time'] <= package['calling_time'] else bill['calling_time'] - package['calling_time']
                    service_fee = package['fee'] + (addition_calling_time * package['extra_calling_rate']) + (bill['sms'] * package['sms_rate'])
                    response = 'your service fee this month is %d baht.' % (service_fee)
                else:
                    account = self._db.find_account(customer)
                    response = 'your account balance is %d baht.' % (account['balance'])
                return response
            else:
                return 'sorry i do not understand your question'

