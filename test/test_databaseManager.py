from unittest import TestCase
from src.database import DatabaseManager

__author__ = 'thanakorn'


class TestDatabaseManager(TestCase):

    def test_find_user_info(self):
        dm = DatabaseManager()
        user = dm.find_user_info('0836990198')
        self.assertEqual(user['firstname'], 'thanakorn')
        self.assertEqual(user['lastname'], 'panyapiang')

    def test_find_user_info_empty_input(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_user_info(''), None)

    def test_find_user_into_invalid_number(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_user_info('082x94938'), None)

    def test_find_user_package(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_user_package('0836990198')['name'], 'Smartphone more net 299')

    def test_find_user_package(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_user_package('0879987123')['name'], 'Happy gang')

    def test_find_user_package_empty_input(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_user_package(''), 'Invalid phone number.')

    def test_find_package_by_category_postpaid(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_package_by_category('calling and internet', 'postpaid').count(), 6)

    def test_find_package_by_category_prepaid(self):
        dm = DatabaseManager()
        self.assertEqual(dm.find_package_by_category('calling and internet', 'prepaid').count(), 3)