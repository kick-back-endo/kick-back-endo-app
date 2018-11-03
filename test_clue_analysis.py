import unittest

from symptom_checker import symptom_checker
from tracker_data_parsers import parse_clue_data


class TestSymptomChecker(unittest.TestCase):

    def test_symptom_checker_positive_long_period(self):
        data_long_period = {'data': [
            {"day": "2016-08-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-02T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-08-03T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-08-04T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-08-05T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-08-06T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-08-07T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-08-08T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-01T00:00:00Z", "pain": ['cramps'], "period": "light"},
            {"day": "2016-09-02T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-03T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-04T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-05T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-06T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-07T00:00:00Z", "pain": [], "period": "medium"},
            {"day": "2016-09-08T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-10-02T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-03T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-10-04T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-10-05T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-10-06T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-10-07T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-10-08T00:00:00Z", "pain": [], "period": "light"},
        ]}

        data = parse_clue_data(data_long_period)

        self.assertTrue(symptom_checker(data))

    def test_symptom_checker_positive_heavy_and_painful(self):
        data_heavy_painful_period = {'data': [
            {"day": "2016-08-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-02T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-03T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-04T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-05T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-09-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-09-02T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-09-03T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-04T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-09-05T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-10-02T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-10-03T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-10-04T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-10-05T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
        ]}

        data = parse_clue_data(data_heavy_painful_period)

        self.assertTrue(symptom_checker(data))
    
    def test_symptom_checker_negative_neither_painful_not_long(self):
        data_ok_period = {'data': [
            {"day": "2016-08-01T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-02T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-03T00:00:00Z", "pain": ['cramps'], "period": "heavy"},
            {"day": "2016-08-04T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-08-05T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-01T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-02T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-03T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-04T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-09-05T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-01T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-02T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-03T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-04T00:00:00Z", "pain": [], "period": "heavy"},
            {"day": "2016-10-05T00:00:00Z", "pain": [], "period": "heavy"},
        ]}

        data = parse_clue_data(data_ok_period)

        self.assertFalse(symptom_checker(data))

    def test_symptom_checker_negative_neither_heavy_nor_long(self):
        data_ok_period = {'data': [
            {"day": "2016-08-01T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-08-02T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-08-03T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-08-04T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-08-05T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-09-01T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-09-02T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-09-03T00:00:00Z", "pain": [], "period": "light"},
            {"day": "2016-09-04T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-09-05T00:00:00Z", "pain": [], "period": 'light'},
            {"day": "2016-10-01T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-10-02T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-10-03T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-10-04T00:00:00Z", "pain": ['cramps'], "period": 'light'},
            {"day": "2016-10-05T00:00:00Z", "pain": ['cramps'], "period": 'light'},
        ]}

        data = parse_clue_data(data_ok_period)

        self.assertFalse(symptom_checker(data))
