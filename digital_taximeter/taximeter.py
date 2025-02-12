import logging

base_idle_rate = 0.02
base_moving_rate = 0.05
base_trip = 2.75


class Taximeter:
    def __init__(self):
        self.total_fare = 0.00

    def adjust_rates(self, demand_level):
        """
        Adjust rates based on demand level.

        Parameters:
        demand_level (str): A string representing the demand level. It should be one of the following: '1', '2', '3'.

        Returns:
        tuple: A tuple containing the adjusted idle rate and moving rate for the given demand level.

        Raises:
        ValueError: If the demand level is not one of the valid options.
        """
        try:
            rates = {
                '1': (base_idle_rate,  base_moving_rate),
                '2': (base_idle_rate + 0.02, base_moving_rate + 0.02),
                '3': (base_idle_rate - 0.01, base_moving_rate - 0.01)
            }

            if demand_level not in rates:
                raise ValueError("Invalid demand level")

            idle_rate, moving_rate = rates[demand_level]
            logging.info(f"Adjusted rates for demand level {demand_level}: idle = {idle_rate} €, moving = {moving_rate} €")
            return idle_rate, moving_rate
        except ValueError as ve:
            logging.error(f"Error in adjust_rates: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in adjust_rates: {e}")
            raise

    def calculate_fare(self, time_elapsed, rate_per_second):
        """
        Calculate the fare for a given time and rate.

        Parameters:
        time_elapsed (float): The time elapsed in seconds. It should be a non-negative number.
        rate_per_second (float): The rate per second for calculating the fare. It should be a positive number.

        Returns:
        float: The calculated fare for the given time and rate.

        Raises:
        ValueError: If the time elapsed is negative.
        """
        try:
            if time_elapsed < 0:
                raise ValueError("Time elapsed cannot be negative")
            fare = time_elapsed * rate_per_second
            logging.debug(f"Calculating fare: {time_elapsed:.2f} seconds * {rate_per_second:.2f} €/second = {fare:.2f} €")
            return fare
        except ValueError as ve:
            logging.error(f"Error in calculate_fare: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in calculate_fare: {e}")
            raise

    def start_trip(self, demand_level, statuses):
        """
        Main trip logic for calculating total fare and adjusting rates.

        Parameters:
        demand_level (str): A string representing the demand level. It should be one of the following: '1', '2', '3'.
        statuses (list): A list of tuples, where each tuple contains a status ('1' for moving, '2' for idle) and a duration (in seconds).

        Returns:
        float: The total fare for the trip.

        Raises:
        Exception: If any unexpected error occurs during the trip calculation.
        """
        try:
            self.total_fare = base_trip
            idle_rate, moving_rate = self.adjust_rates(demand_level)
            logging.info(f"Starting trip with demand level {demand_level}. Rates: idle = {idle_rate} €, moving = {moving_rate} €")

            for status, duration in statuses:
                if status not in ['1', '2']:
                    logging.warning(f"Invalid status {status} in trip status list.")
                    continue

                if duration < 0:
                    logging.warning(f"Invalid duration {duration} found. Skipping this status segment.")
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


