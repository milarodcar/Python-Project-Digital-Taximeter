import time
import logging

class Trip:
    def __init__(self, taximeter):
        self.taximeter = taximeter

    def get_demand_level(self):  # sourcery skip: class-extract-method
        """Get the demand level from user input."""
        while True:
            try:
                demand = input("\nWhat is the demand level? \n1 normal\n2 high\n3 low\n ").strip()
                if demand in ['1', '2', '3']:
                    logging.info(f"Demand level selected: {demand}")
                    return demand
                else:
                    logging.warning("Invalid demand level. Please enter 1,2 or 3")
                    print("Invalid demand level. Please enter 1, 2 or 3.")
                    raise ValueError("Invalid demand level")        
            except Exception as e:
                logging.error(f"Error in get_demand_level: {e}")
                print("An unexpected error occurred while getting the demand. Please try again.")

    def get_trip_status(self):
        """Get the taxi status from user input. (moving, idle or finish)"""
        while True:
            try:
                status = input("\nWhat is the taxi status? \n1 moving\n2 idle\n3 finish\n ").strip()
                if status in ['1', '2', '3']:
                    logging.info(f"Taxi status selected: {status}")
                    return status
                else:        
                    logging.warning("Invalid taxi status. Please enter 1 for moving, 2 for idle or 3 for finish")
                    print("Invalid taxi status. Please enter 1 for moving, 2 for idle or 3 finish.")
                    raise ValueError("Invalid taxi status")
            except Exception as e:
                logging.error(f"Error in get_trip_status: {e}")
                print("An unexpected error occurred while getting the taxi status. Please try again.")

    def start(self):
        """Start the trip process and interact with the user."""
        statuses = []
        logging.info("Starting the trip process")
        try:
            demand_level = self.get_demand_level()
            logging.info(f"Starting trip calculation with demand level {demand_level}.")
        except Exception as e:
            logging.error(f"Error in start: {e}")
            print("An unexpected error occurred while starting the trip. Please try again.")
            return
    
        while True:
            try:
                status = self.get_trip_status()
                if status == '3':
                    total_fare = self.taximeter.start_trip(demand_level, statuses)
                    print(f"\nTrip ended. Total fare: {total_fare:.2f} €")
                    logging.info(f"Trip ended. Total fare: {total_fare:.2f} €.")
                    logging.info("User chose to finish the trip")
                    break

                elif status in ['1', '2']:
                    start_time = time.time()
                    logging.info(f"Start time :{start_time}")
                    input(f"Press Enter when the taxi is no longer {('moving' if status == '1' else 'idle')}.")
                    end_time = time.time()
                    time_elapsed = end_time - start_time
                    statuses.append((status, time_elapsed))

                    logging.info(f"Added status: {status} for {time_elapsed:.2f} seconds")

            except KeyboardInterrupt:
                logging.error("User interrupted the process")
                print("\nProcess interrupted. Exiting the application.")
                break
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print("An unexpected error occurred. Please try again.")
                break

            

