from aviationweatherapi import aviationweatherapi
from aviationweatherapi.get_airport_info import get_airport_info
from aviationweatherapi.get_airport_metar import get_airport_metar
from aviationweatherapi.get_average_elevation_by_state import get_average_elevation_by_state
from aviationweatherapi.help_ import help_
import unittest
from io import StringIO
import sys

class AirportInfoTest(unittest.TestCase):
    def test_get_airport_info(self):
        result = get_airport_info('KLAX')
        self.assertIn('Los Angeles', result)
        self.assertIn('LAX', result)
        
class AirportMetarTest(unittest.TestCase):
    def test_get_airport_metar(self):
        result = get_airport_metar('KLAX')
        self.assertIn('METAR', result)
        self.assertIn('KLAX', result)

class AverageElevationTest(unittest.TestCase):
    def test_get_average_elevation_by_state(self):
        result = get_average_elevation_by_state('CA')
        self.assertIsInstance(result, float)
        
class TestHelpFunction(unittest.TestCase):
    def test_help_function(self):
        capturedOutput = StringIO()         
        sys.stdout = capturedOutput         
        show_help()                          
        sys.stdout = sys.__stdout__          
        output = capturedOutput.getvalue()   

        self.assertIn('get_airport_info', output) 
        self.assertIn('get_airport_metar', output)
        self.assertIn('get_average_elevation_by_state', output)

if __name__ == '__main__':
    unittest.main()

