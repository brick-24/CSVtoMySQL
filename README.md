# CSV to MySQL

[![Build Status](https://img.shields.io/github/actions/workflow/status/COMMANDO2406/CSVtoMySQL/test.yml?branch=main)](https://github.com/COMMANDO2406/CSVtoMySQL/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

# Demo
![image](https://github.com/user-attachments/assets/e012b8b9-b0fb-4d0c-a07c-b0c9cf3f0bc8)



## Documentation

Official documentation is available at:
https://commando2406.github.io/CSVtoMySQL/

This project helps import CSV data into MySQL database by:
- Creating database if not exists
- Creating table from CSV headers
- Importing CSV data automatically

## Features

- Connect to MySQL database
- Check and create database if it doesn't exist
- Create table based on CSV header
- Import CSV data into MySQL table

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- MySQL server
- `mysql-connector-python` library

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/COMMANDO2406/CSVtoMySQL.git
   cd CSVtoMySQL
   ```

2. Install the required Python packages:

   ```bash
   pip install mysql-connector-python
   ```

3. Create a `config.py` file:

   ```python
   # config.py
   host = 'your_mysql_host'
   user = 'your_mysql_user'
   password = 'your_mysql_password'
   ```

4. Prepare your CSV file:
   Ensure you have a CSV file named `main.csv` in the same directory as the script. The CSV file should have a header row with column names matching the ones you will specify in the script.

### Important Notes
- Ensure MySQL server is running before execution
- Update config.py with correct credentials
- CSV file must be named main.csv

## How it works
1. Reads CSV file
2. Connects to MySQL
3. Creates database if not exists
4. Creates table based on CSV header
5. Inserts data row by row

## Example

Here is an example of how to use the script:

1. **Prepare your CSV file (`main.csv`):**

   ```csv
   name,age,city
   Alice,30,New York
   Bob,25,Los Angeles
   ```

2. **Run the script:**

   ```bash
   python csv_to_mysql.py
   ```

3. **Enter the following when prompted:**

   ```
   Enter database name: my_database
   Enter table name: people
   Enter column names (Separated by commas): name,age,city
   ```

4. **The script will output:**

   ```
   Connected successfully
   Database 'my_database' created successfully
   Data imported successfully.
   ```

## Troubleshooting
- If connection fails → check MySQL credentials
- If table error → ensure column names match CSV header