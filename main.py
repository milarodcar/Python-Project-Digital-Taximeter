import random
import string
from digital_taximeter.taximeter import Taximeter
from digital_taximeter.trip import Trip
from digital_taximeter.history import History
import logging
import os
from datetime import datetime

def generate_trip_id():
    """
    Generate a unique trip_id using random alphanumeric characters.

    This function generates a unique trip ID by combining two random uppercase letters and six random digits.
    The generated trip ID is used to identify individual trips in the taximeter application.

    Parameters:
    None

    Returns:
    str: A unique trip ID consisting of two uppercase letters and six digits.
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{letters}{digits}"

def clear_terminal():
    """
    Clear the terminal screen for better user experience.

    This function uses the appropriate command to clear the terminal screen based on the operating system.
    On Windows, it uses the 'cls' command, while on Unix-based systems, it uses the 'clear' command.

    Parameters:
    None

    Returns:
    None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """
    Display welcome message and instructions.

    This function prints a welcome message and instructions to the console.
    The message includes information about the program's purpose and how to interact with it.

    Parameters:
    None

    Returns:
    None
    """
    print("\nWelcome to the Digital Taximeter")
    print("This program calculates your trip fare based on idle and moving time.")
    print("\nInstructions:")
    print("- Start a trip")
    print("- Choose demand level: 1=Normal, 2=High, 3=Low")
    print("- During trip: 1=Moving, 2=Idle, 3=Finish")
    print("- You can do multiple trips without exiting\n")

def setup_logging():
    """
    Configure logging with timestamped filename.

    This function sets up logging for the application. It creates a log file with a timestamped name in the 'Logs' directory.
    The log file will store information at the INFO level, including timestamps, log levels, and messages.

    Parameters:
    None

    Returns:
    None

    Raises:
    None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join("Logs", f"taximeter_{timestamp}.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_filename,
        filemode='a'
    )

def main():
    """
    The main function of Digital Taximeter application.

    This function initializes the application, sets up logging, clears the terminal, and displays the welcome message.
    It then creates instances of the Taximeter class, logs the application start and enters a loop
    to handle user input and manage trips.

    Parameters:
    None

    Returns:
    None

    """
    setup_logging()
    clear_terminal()
    show_welcome()

    taximeter = Taximeter()


    logging.info("Application started")

    while True:
        try:
            option = input("\nMain Menu\n1. Start new trip\n2. Exit\nYour choice: ").strip()

            if option == '1':
                # Call the generate_trip_id function to get a new unique ID
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
