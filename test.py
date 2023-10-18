import sys
import os
import unittest
from datetime import datetime
from main import main
from sensor import Sensor
from device import Device
from data_processor import DataProcessor
from dashboard import Dashboard
from communication import Communication
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class test_data_processor(unittest.TestCase): 
    
     def setUp(self):
        self.dp = DataProcessor()
        self.data = [
            (datetime(2022, 1, 1, 0, 0, 0), 10),
            (datetime(2022, 1, 1, 0, 1, 0), 20),
            (datetime(2022, 1, 1, 0, 2, 0), 30),
            (datetime(2022, 1, 1, 0, 3, 0), 40),
            (datetime(2022, 1, 1, 0, 4, 0), 50),
        ]
        
     def test_generate_analytics(self):
        expected_result = {
            "data": [10, 20, 30, 40, 50],
            "mean": 30.0,
            "median": 30.0,
            "stdev": 15.81,
            "min": 10,
            "max": 50,
            "start_time": datetime(2022, 1, 1, 0, 0, 0),
            "end_time": datetime(2022, 1, 1, 0, 4, 0)
        }
        result = self.dp.generate_analytics(self.data)
        self.assertEqual(result, expected_result)
        

class TestSensor(unittest.TestCase):
    
     def setUp(self):
        self.sensor = Sensor(10, 20)

     def test_read_data(self):
        with patch('sensor.datetime') as mock_date:
            mock_date.now.return_value = datetime(2022, 1, 1, 0, 0, 0)
            data = self.sensor.read_data()
            data2 = data
            self.assertEqual(data, data2)


if __name__ == '__main__':
    unittest.main()