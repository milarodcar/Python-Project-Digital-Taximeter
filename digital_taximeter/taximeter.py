import time
import logging

class Taximeter:
    def __init__(self):
        self.base_idle_rate = 0.02
        self.base_moving_rate = 0.05
        self.total_fare = 0.0

    def adjust_rates(self, demand_level):
        """Adjust rates based on demand level"""
        try:
            idle_rate = self.base_idle_rate
            moving_rate = self.base_moving_rate

            if demand_level == '3':
                idle_rate -= 0.01
                moving_rate -= 0.01
                logging.info("Adjusted rates for demand level 3 (low)")
            elif demand_level == '2':
                idle_rate += 0.02
                moving_rate += 0.02
                logging.info("Adjusted rates for demand level 2 (high)")
            elif demand_level == '1':
                logging.info("Adjusted rates for demand level 1 (normal)")
            else:
                raise ValueError("Invalid demand level")  # Raise an error if an invalid level is passed

            return idle_rate, moving_rate
        except ValueError as ve:
            logging.error(f"ValueError in adjust_rates: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in adjust_rates: {e}")
            raise

    def calculate_fare(self, time_elapsed, rate_per_second):
        """Calculate the fare for a given time and rate"""
        try:
            if time_elapsed < 0:
                raise ValueError("Time elapsed cannot be negative.")
            fare = time_elapsed * rate_per_second
            logging.debug(f"Calculating fare: {time_elapsed:.2f} seconds * {rate_per_second:.2f} €/second = {fare:.2f} €")
            return fare
        except ValueError as ve:
            logging.error(f"ValueError in calculate_fare: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in calculate_fare: {e}")
            raise

    def start_trip(self, demand_level, statuses):
        """Main trip logic for calculating total fare and adjusting rates"""
        try:
            idle_rate, moving_rate = self.adjust_rates(demand_level)
            logging.info(f"Trip started with demand level {demand_level}. Rates: idle = {idle_rate} €, moving = {moving_rate} €")

            for status, duration in statuses:
                if status not in ['1', '2']:  # Ensure the status is either moving or idle
                    logging.warning(f"Invalid status {status} in trip status list.")
                    continue

                if duration < 0:
                    logging.warning(f"Negative duration {duration} found. Skipping this status segment.")
                    continue

                rate = moving_rate if status == '1' else idle_rate
                fare = self.calculate_fare(duration, rate)
                self.total_fare += fare
                logging.info(f"Taxi is {('moving' if status == '1' else 'idle')} for {duration:.2f} seconds. Fare for this segment: {fare:.2f} €")

            logging.info(f"Trip ended. Total fare: {self.total_fare:.2f} €")
            return self.total_fare
        except Exception as e:
            logging.error(f"Unexpected error in start_trip: {e}")
            raise
