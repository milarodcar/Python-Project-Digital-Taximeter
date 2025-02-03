import unittest
from unittest.mock import patch
from digital_taximeter.taximeter import Taximeter
import logging

class TestTaximeter(unittest.TestCase):
    def setUp(self):
        self.taximeter = Taximeter()
        logging.disable(logging.CRITICAL)

    def test_calculate_fare_valid_input(self):
        fare = self.taximeter.calculate_fare(10, 0.05)
        self.assertEqual(fare, 0.5)

    def test_calculate_fare_negative_time(self):
        with self.assertRaises(ValueError):
            self.taximeter.calculate_fare(-5, 0.05)

    def test_adjust_rates_normal(self):
        idle, moving = self.taximeter.adjust_rates('1')
        self.assertEqual((idle, moving), (0.02, 0.05))

    def test_adjust_rates_high(self):
        idle, moving = self.taximeter.adjust_rates('2')
        self.assertEqual((idle, moving), (0.04, 0.07))

    def test_adjust_rates_low(self):
        idle, moving = self.taximeter.adjust_rates('3')
        self.assertEqual(round(idle, 2), 0.01)
        self.assertEqual(round(moving, 2), 0.04)

    def test_adjust_rates_invalid_level(self):
        with self.assertRaises(ValueError):
            self.taximeter.adjust_rates('invalid')

    @patch('logging.Logger.warning')
    def test_start_trip_invalid_status(self, mock_logger):
        statuses = [('invalid_status', 10)]
        self.taximeter.start_trip('1', statuses)
        mock_logger.assert_called_with("Invalid status invalid_status in trip status list.")

    @patch('logging.Logger.warning')
    def test_start_trip_negative_duration(self, mock_logger):
        statuses = [('1', -5)]
        self.taximeter.start_trip('1', statuses)
        mock_logger.assert_called_with("Invalid duration -5 found. Skipping this status segment.")

if __name__ == "__main__":
    unittest.main()
