import random
import string
from digital_taximeter.taximeter import Taximeter
from digital_taximeter.trip import Trip
from digital_taximeter.history import History
import logging
import os
from datetime import datetime

def generate_trip_id():
    """Generate a unique trip_id using random alphanumeric characters"""
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{letters}{digits}"

def clear_terminal():
    """Clear the terminal screen for better user experience"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """Display welcome message and instructions"""
    print("\nWelcome to the Digital Taximeter")
    print("This program calculates your trip fare based on idle and moving time.")
    print("\nInstructions:")
    print("- Start a trip")
    print("- Choose demand level: 1=Normal, 2=High, 3=Low")
    print("- During trip: 1=Moving, 2=Idle, 3=Finish")
    print("- You can do multiple trips without exiting\n")

def setup_logging():
    """Configure logging with timestamped filename"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join("Logs", f"taximeter_{timestamp}.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_filename,
        filemode='a'
    )

def main():
    setup_logging()
    clear_terminal()
    show_welcome()

    taximeter = Taximeter()
    history = History()

    logging.info("Application started")

    while True:
        try:
            option = input("\nMain Menu\n1. Start new trip\n2. Exit\nYour choice: ").strip()

            if option == '1':
                # Call the generate_trip_id function to get a new unique ID
                total_fare = 0
                trip_id = generate_trip_id()
                logging.info(f"Starting new trip with trip_id: {trip_id}")
                trip = Trip(trip_id=trip_id, taximeter=taximeter)  # Pass the trip_id to the Trip class
                trip.start(taximeter)  # Use Trip's start method to begin the trip
            elif option == '2':
                logging.info("User exited application")
                print("\nThank you for using the Digital Taximeter. Goodbye!")
                break
            else:
                logging.warning(f"Invalid menu input: {option}")
                print("Invalid choice. Please enter 1 or 2.")

        except KeyboardInterrupt:
            logging.warning("Process interrupted by user")
            print("\nOperation cancelled. Returning to main menu...")
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}", exc_info=True)
            print(f"\nAn error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    main()
