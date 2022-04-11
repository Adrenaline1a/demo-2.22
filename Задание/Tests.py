import unittest
import functioins as fun


class SqlTest(unittest.TestCase):
    """Тест операций по работе с SQL"""
    
    def test_sql_table(self):
        self.assertEqual(fun.sql_table(), 1)

    def test_sql_connection(self):
        self.assertEqual(fun.sql_connection(), 1)
    
    def test_adding(self):
        self.assertEqual(fun.sql_connection(), 1)

    def test_selecting(self):
        self.assertEqual(fun.sql_connection(), 1)

    def test_table(self):
        self.assertEqual(fun.sql_connection(), 1)

    def test_inf(self):
        self.assertEqual(fun.sql_connection(), 1)
