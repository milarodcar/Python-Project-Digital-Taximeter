import unittest
from unittest.mock import patch
from digital_taximeter.taximeter import Taximeter
from digital_taximeter.trip import Trip
import logging

class TestTrip(unittest.TestCase):
    def setUp(self):
        self.taximeter = Taximeter()
        self.trip_id = 'test_trip_id'
        self.trip = Trip(self.trip_id, self.taximeter)
        logging.disable(logging.CRITICAL)

    @patch('time.time', side_effect=[100, 110, 115, 120])  # 10s moving + 5s idle
    @patch('builtins.input', side_effect=['1', '1', '', '2', '', '3'])
    def test_normal_demand_trip(self, mock_input, mock_time):
        with patch('builtins.print') as mock_print:
            self.trip.start(self.taximeter)
            mock_print.assert_any_call("\nTrip ended. Your total fare is 3.35 €.")

    @patch('time.time', side_effect=[200, 210])  # No time elapsed
    @patch('builtins.input', side_effect=['3', '3'])
    def test_empty_trip(self, mock_input, mock_time):
        with patch('builtins.print') as mock_print:
            self.trip.start(self.taximeter)
            mock_print.assert_any_call("No trip data to finalize. Please record some movement or idle time first.")

    @patch('builtins.input', side_effect=['invalid', '1', '3'])
    def test_retry_invalid_demand_level(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.trip.start(self.taximeter)
            mock_print.assert_any_call("Invalid option. Please try again.")

    @patch('logging.info')
    @patch('time.time', side_effect=[100, 100])  # Zero duration
    def test_status_segment_logging(self, mock_time, mock_logger):
        with patch('builtins.input', side_effect=['1', '1', '', '3']):
            self.trip.start(self.taximeter)
        mock_logger.assert_any_call("Taxi is moving for 0.00 seconds. Fare for this segment: 0.00 €")

    @patch('logging.Logger.error')
    @patch('builtins.input', side_effect=['1', 'invalid', '3'])
    def test_retry_invalid_status(self, mock_input, mock_logger):
        with patch('builtins.print'):  # Suppress print output
            self.trip.start(self.taximeter)
        mock_logger.assert_any_call("Invalid input: Invalid input invalid")

if __name__ == "__main__":
    unittest.main()