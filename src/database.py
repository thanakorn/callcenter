__author__ = 'thanakorn'

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class DatabaseManager(object):
    """  Class for handle DB operation """

    def __init__(self):
        """ Initial MongoDB client """
        client = MongoClient('localhost', 27017)
        db = client['callcenter']
        self.customers = db['customers']
        self.packages = db['packages']
        self.enhanced_packages = db['enhanced_packages']
        self.bills = db['bills']
        self.accounts = db['accounts']

    def find_user_info(self, phone_number):
        """ Find customer information """
        return self.customers.find_one({'phone_number': phone_number})

    def find_user_package(self, phone_number):
        """ Find current user package """
        customer = self.customers.find_one({'phone_number': phone_number})
        if customer is None:
            return 'Invalid phone number.'

        try:
            bills = self.bills.find({'customer': customer['_id']}).sort('payment_date', -1)
            package_id = bills[0]['package']
        except ValueError:
            account = self.accounts.find_one({'customer': customer['_id']})
            package_id = account['package']

        return self.packages.find_one({'_id': ObjectId(package_id)})


