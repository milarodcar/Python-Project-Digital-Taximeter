import time
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="taximeter.log",
    filemode="a",
)

def show_welcome():
    logging.info("Displaying welcome message")
    print("Welcome to the Digital Taximeter")
    print("This program calculates your trip fare based on idle and moving time.")
    print("Instructions:")
    print("1. Start a trip.")
    print("2. Indicate if the taxi is idle or moving.")
    print("3. End the trip to see the total fare.")
    print("You can start a new trip without exiting the program. \n")

def calculate_fare(time_elapsed, rate_per_second):
    return time_elapsed * rate_per_second
    logging.debug(f"Calculating fare: {time_elapsed:.2f} seconds * {rate_per_second:.2f} €/second = {fare:.2f} €")
    return fare

def start_trip():
    logging.info("Starting a new trip")
    print("\n Trip started. Have a good journey!")
    total_fare = 0.0
    while True:
        status= input("\nWhat is the taxi doing? (idle/moving/finish): ").strip().lower()

        if status == "finish":
            logging.info("Trip ended. Total fare: {total_fare:.2} €")
            print(f"\nTrip ended. Your total fare is ${total_fare:.2f} €.")
            break
        elif status == "idle" or status == "moving":
            start_time = time.time()
            input(f"Press Enter when the taxi is no longer {status}... ")
            end_time = time.time()
            time_elapsed = end_time - start_time

            if status == "idle":
                fare = calculate_fare(time_elapsed, 0.02)
            else:
                fare = calculate_fare(time_elapsed, 0.05)

            total_fare += fare
            logging.info(f"Status {status} | Time: {time_elapsed:.2f} seconds | Total fare so far: {total_fare:.2f} €")
            print(f"Time {status}: {time_elapsed:.2f} seconds | Fare for this segment: {fare:.2f} € |Total fare so far: {total_fare:.2f} €")
        
        else:
            logging.warning(f"Invalid input {status}")
            print("Invalid input. Please enter 'idle', 'moving', or 'finish'.")

def main():
    logging.info("Digital Taximeter started")
    show_welcome()
    while True:
        option = input("\nWhat would you like to do? (start/exit): ").strip().lower()
        if option == "start":
            start_trip()
        elif option == "exit":
            logging.info("Digital Taximeter exited")
            print("Thank you for using the Digital Taximeter. Goodbye!")
            break
        else:
            logging.warning(f"Invalid input {option}")
            print("Invalid input. Please enter 'start' or 'exit'.")


if __name__ == "__main__":
    main()