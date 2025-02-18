import logging
import time

class Trip:
    def __init__(self, trip_id, taximeter, start_time=None, end_time=None, moving_time=0, idle_time=0, fare=0):
        self.trip_id = trip_id
        self.taximeter = taximeter
        self.start_time = start_time
        self.end_time = end_time
        self.moving_time = moving_time
        self.idle_time = idle_time
        self.fare = fare

    def get_user_input(self, prompt, valid_options):
        """
        Handles user input validation for specific prompts.

        Parameters:
        prompt (str): The prompt message to display to the user.
        valid_options (list): A list of valid options that the user can select.

        Returns:
        str: The user's selected option.

        Raises:
        ValueError: If the user's input is not in the valid_options list.
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if user_input in valid_options:
                    logging.info(f"User selected: {user_input}")
                    return user_input
                else:
                    raise ValueError(f"Invalid input {user_input}")
            except ValueError as e:
                logging.error(f"Invalid input: {e}")
                print("Invalid option. Please try again.")

    def start(self, taximeter):
        """
        Start the trip process and interact with the user.

        Parameters:
        taximeter (Taximeter): An instance of the Taximeter class representing the taximeter for this trip.

        Returns:
        None

        The function starts the trip process by prompting the user to select the demand level and taxi status.
        It records the taxi status and time elapsed for each status change.
        If the user selects "Finish", it calculates the total fare based on the demand level and recorded statuses.
        The function handles exceptions and provides appropriate error messages.
        """
        statuses = []
        logging.info("Starting the trip process")

        try:
            demand_level = self.get_user_input("\nWhat is the demand level? \n1 normal\n2 high\n3 low\n", ['1', '2', '3'])
            logging.info(f"Demand level selected: {demand_level}")
        except Exception as e:
            logging.error(f"Error starting trip: {e}")
            print("An unexpected error occurred while starting the trip. Please try again.")
            return

        while True:
            try:
                status = self.get_user_input("\nWhat is the taxi status? \n1 moving\n2 idle\n3 finish\n", ['1', '2', '3'])

                if status == '3':  # User selects "Finish"
                    if not statuses:
                        print("No trip data to finalize. Please record some movement or idle time first.")
                        logging.warning("Attempted to finish trip without any statuses.")
                    else:
                        total_fare = taximeter.start_trip(demand_level, statuses)
                        print(f"\nTrip ended. Your total fare is {total_fare:.2f} €.")
                        logging.info(f"Trip ended. Total fare: {total_fare:.2f} €")
                        
                    break

                elif status in ['1', '2']:
                    start_time = time.time()
                    input(f"Press Enter when the taxi is no longer {('moving' if status == '1' else 'idle')}.")
                    end_time = time.time()
                    time_elapsed = end_time - start_time
                    statuses.append((status, time_elapsed))

                    logging.info(f"Added status: {status} for {time_elapsed:.2f} seconds")

            except KeyboardInterrupt:
                logging.error("User interrupted the application")
                print("\nProcess interrupted. Exiting the application.")
                break
            except Exception as e:
                logging.error(f"Error in trip process: {e}")
                print("An unexpected error occurred. Please try again.")
                break