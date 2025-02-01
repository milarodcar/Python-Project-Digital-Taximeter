import time
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="taximeter.log",
    filemode="a",
)

class Taximeter:
    def __init__(self):
        self.base_idle_rate = 0.02
        self.base_moving_rate = 0.05
        self.total_fare = 0.0
    
    def adjust_rates(self, demand_level):
        """Adjust rates based on demand level"""
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
        else:
            logging.info("Adjusted rates for demand level 1 (normal)")
        
        return idle_rate, moving_rate
    
    def calculate_fare(self, time_elapsed, rate_per_second):
        fare = time_elapsed * rate_per_second
        logging.debug(f"Calculating fare: {time_elapsed:.2f} seconds * {rate_per_second:.2f} €/second = {fare:.2f} €")
        return f

def show_welcome():
    logging.info("Displaying welcome message")
    print("Welcome to the Digital Taximeter")
    print("This program calculates your trip fare based on idle and moving time.")
    print("Instructions:")
    print("- Start a trip.")
    print("- To choose demand use 1 for normal, 2 for high, 3 for low.")
    print("- To choose state use 1 for moving, 2 for idle, 3 to finish.")
    print("- You can do multiple trips without exiting\n.")

def calculate_fare(time_elapsed, rate_per_second):
    fare = time_elapsed * rate_per_second
    logging.debug(f"Calculating fare: {time_elapsed:.2f} seconds * {rate_per_second:.2f} €/second = {fare:.2f} €")
    return fare

def start_trip():
    logging.info("Starting a new trip")
    print("\n Trip started. Have a good journey!")

    #Define default rates
    base_idle_rate = 0.02
    base_moving_rate = 0.05

    #Initialize the rates
    idle_rate = base_idle_rate
    moving_rate = base_moving_rate

    #Get demand level
    while True:
        demand = input("\nWhat is the demand level? \n1 normal\n2 high\n3 low\n ").strip()
        if demand in ['1', '2', '3']:
            break
        logging.warning("Invalid demand level. Please enter 1,2 or 3")
        print("Invalid demand level. Please enter 1, 2 or 3.")

        #Adjust rates based on demand level
        idle_rate = base_idle_rate
        moving_rate = base_moving_rate

        if demand == '3':
            idle_rate -= 0.01
            moving_rate -= 0.01
            logging.info("Adjusted rates for demand level 3 (low)")
        elif demand == '2':
            idle_rate += 0.02
            moving_rate += 0.02
            logging.info("Adjusted rates for demand level 2 (high)")
        else:
            logging.info("Adjusted rates for demand level 1 (normal)")

    total_fare = 0.0
    while True:
        status= input("\nWhat is the taxi doing? \n1 moving\n2 idle\n3 finish\n").strip()

        if status == '3':
            logging.info(f"Trip ended. Total fare: {total_fare:.2} €")
            print(f"\nTrip ended. Your total fare is ${total_fare:.2f} €.")
            break
        elif status in ['2', '1']:
            start_time = time.time()
            input(f"Press Enter when the taxi is no longer {('moving' if status == '1' else 'idle')}.")
            end_time = time.time()
            time_elapsed = end_time - start_time

            #Calculate fare based on the current status
            rate = moving_rate if status == '1' else idle_rate
            fare = calculate_fare(time_elapsed, rate)

            total_fare += fare
            logging.info(f"Status {status} | Time: {time_elapsed:.2f} seconds | Total fare so far: {total_fare:.2f} €")
            print(f"Time {('moving' if status == '1' else 'idle')}: {time_elapsed:.2f} seconds | Fare for this segment: {fare:.2f} € | Total fare so far: {total_fare:.2f} €")

        else:
            logging.warning(f"Invalid input {status}")
            print("Invalid input. Please enter '1' for moving, '2' for idle, or '3' to finish.")

def main():
    logging.info("Digital Taximeter started")
    show_welcome()
    while True:
        option = input("\nWhat would you like to do? \n1 start\n2 exit\n").strip()
        if option == '1':
            start_trip()
        elif option == '2':
            logging.info("Digital Taximeter exited")
            print("Thank you for using the Digital Taximeter. Goodbye!")
            break
        else:
            logging.warning(f"Invalid input {option}")
            print("Invalid input. Please enter 1 to start or 2 to exit.")


if __name__ == "__main__":
    main()