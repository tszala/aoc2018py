import unittest
from datetime import datetime


import day4

def fun(x):
    return x + 1

class Day4Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3),4)

    def test2(self):
        self.assertEqual(day4.line_to_action("[1518-03-14 00:34] falls asleep"),"SLEEP")

    def test_get_minutes_between_dates_returns_empty_list_for_equal_dates(self):
        d1=datetime(2018,12,29,22,22)
        d2=datetime(2018,12,29,22,22)
        self.assertEqual(day4.get_minutes_between_dates(d1,d2), [])

    def test_get_minutes_between_dates_returns_not_empty_list_for_inequal_dates(self):
        d1=datetime(2018,12,29,22,22)
        d2=datetime(2018,12,29,22,23)
        self.assertEqual(day4.get_minutes_between_dates(d1,d2), [22])
