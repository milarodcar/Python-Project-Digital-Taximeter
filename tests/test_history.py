import unittest
from unittest.mock import patch, mock_open
from digital_taximeter.history import History
from digital_taximeter.trip import Trip
import os
import json

class TestHistory(unittest.TestCase):
    def setUp(self):
        """Setup test variables."""
        self.history = History(log_file="test_log.log", history_file="test_history.json")

        @patch("builtins.open", new_callable=mock_open, read_data="Starting new trip\n Taxi is moving for 60.0 seconds\nTRip ended. Total fare: 10.0 €")
        @patch("os.path.exists", return_value=True)


        def test_load_history(self, mock_exists, mock_open):
            "Test the load_history method"
            self.history.load_history()

            mock_open.assert_called_with('test_log.log')
            self.assertEqual(len(self.history.trips), 1)
            trip = self.history.trips[0]
            self.assertEqual(trip.trip_id, 1)
            self.assertEqual(trip.fare,10.0)
            self.assertEqual(trip.moving_time, 60.0)

        @patch("builtins.open", new_callable=mock_open)
        def test_save_history(self, mock_open):
            """Test the save history method."""
            trip = Trip(trip_id=1, start_time="2025-02-04 10:00", end_time="2025-02-04 10:30", moving_time=60.0, idle_time=30.0, fare=15.0)
            self.history.trips.append(trip)

            self.history.save_history()

            mock_open.assert_called_with('test_history.json', 'w')
            mock_open.return_value.write.assert_called_once_with('[\n    {\n        "trip_id": 1,\n        "start_time": "2025-02-04 10:00",\n        "end_time": "2025-02-04 10:30",\n        "moving_time": 60.0,\n        "idle_time": 30.0,\n        "fare": 15.0\n    }\n]')

        @patch("builtins.print")
        def test_show_history(self, mock_print):
            """Test the show_history method."""
            trip = Trip(trip_id=1, start_time="2025-02-04 10:00", end_time="2025-02-04 10:30", moving_time=60.0, idle_time=30.0, fare=15.0)
            self.history.trips.append(trip)

            self.history.show_history()

            mock_print.assert_called_with("Trip ID: 1, Start: 2025-02-04 10:00, End: 2025-02-04 10:30, Moving time: 60.0s, Idle time: 30.0s, Fare: 15.0€")

            @patch("os.path.exists", return_value=False)
            @patch("builtins.open", new_callable=mock_open)
            def test_load_history_no_log_file(self, mock_open, mock_exists):
                """When the load file does not exist"""
                self.history.load_history()
                mock_open.assert_called_once_with("test_log.log",'w')
                self.assertEqual(len(self.history.trips), 0)

if __name__ == '__main__':
    unittest.main()