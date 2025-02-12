# Python-Project-Digital-Taximeter

A Python project that simulates a digital taximeter system.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Project Structure

```
Python-Project-Digital-Taximeter/
│   .coverage
│   main.py
│   poetry.lock
│   pyproject.toml
│   README.md
│
├───digital_taximeter/
│       history.py
│       taximeter.py
│       trip.py
│       __init__.py
│
├───Logs/
│       app.log
│       history.json
│       taximeter_2025-02-05_16-54-26.log
│
└───tests/
        test_history.py
        test_taximeter.py
        test_trip.py
        __init__.py
```

## Features

- Simulates a digital taximeter system.
- Tracks the start and end of trips.
- Calculates the total fare based on moving and idle time.
- Stores trip history in a log file and a JSON file.

## Installation

To install the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Python-Project-Digital-Taximeter.git
   ```

2. Navigate to the project directory:
   ```
   cd Python-Project-Digital-Taximeter
   ```

3. Install the required dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

To use the digital taximeter system, follow these steps:

1. Run the `main.py` file:
   ```
   python main.py
   ```

2. The program will prompt you to enter the start and end times of the trip.

3. After entering the times, the program will calculate the total fare and display it.

4. The trip details will be logged in the `Logs/app.log` file and stored in the `Logs/history.json` file.

## Testing

To run the test suite, execute the following command:

```
poetry run pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Please note that this README file is a template and may need to be adjusted based on your specific project requirements.