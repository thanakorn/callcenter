from unittest import TestCase
from src.database import DatabaseManager

__author__ = 'thanakorn'


class TestDatabaseManager(TestCase):

    def test_findUserPackage(self):
        dm = DatabaseManager()
        self.assertEqual(dm.findUserPackage('0836990198')['name'],'Smartphone more net 299')
