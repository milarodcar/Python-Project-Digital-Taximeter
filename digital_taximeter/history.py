import re
import json
import logging
import os
from digital_taximeter.trip import Trip

class History:
    def __init__(self, log_file='app.log', history_file='history.json'):
        self.trips = []
        self.log_file = log_file
        self.history_file = history_file
        self.load_history()

    def load_history(self):
        """Read the logs to extract trips"""
        if not os.path.exists(self.log_file):
            logging.info(f"{self.log_file} not found. Creating a new log file")
            with open(self.log_file, 'w') as file:
                file.write("")

        with open(self.log_file, 'r') as file:
            logs = file.readlines()

        trip_pattern = re.compile(r"Trip ended\. Total fare: ([\d.]+) €")
        moving_pattern = re.compile(r"Taxi is moving for ([\d.]+) seconds")
        idle_pattern = re.compile(r"Taxi is idle for ([\d.]+) seconds")
        start_pattern = re.compile(r"Starting new trip")
        end_pattern = re.compile(r"Trip ended")

        trip_id = 0
        start_time = None
        moving_time = 0
        idle_time = 0
        fare = 0

        for log in logs:
            if start_pattern.search(log):
                trip_id += 1
                start_time = log.split(' - ')[0]  # Extract the date and time from the log
                moving_time = 0
                idle_time = 0
                fare = 0
            elif moving_pattern.search(log):
                moving_time = float(moving_pattern.search(log).group(1))
            elif idle_pattern.search(log):
                idle_time = float(idle_pattern.search(log).group(1))
            elif trip_ended := trip_pattern.search(log):
                fare = float(trip_ended.group(1))
                end_time = log.split(' - ')[0]
                trip = Trip(trip_id, start_time, end_time, moving_time, idle_time, fare)
                self.trips.append(trip)

        self.save_history()

    def save_history(self):
        """Save trip details to a JSON file"""
        with open(self.history_file, 'w') as f:
            json.dump([trip.__dict__ for trip in self.trips], f, indent=4)

    def show_history(self):
        """Display the trip history"""
        if not self.trips:
            print("No trips found.")
        for trip in self.trips:
            print(f"Trip ID: {trip.trip_id}, Start: {trip.start_time}, End: {trip.end_time}, "f"Moving time: {trip.moving_time}s, Idle time: {trip.idle_time}s, Fare: {trip.fare}€")
