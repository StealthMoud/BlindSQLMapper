# SQL Injection Exploitation Tool

## Overview

This tool is designed to assist in the exploitation of **Boolean-based** and **Time-based** SQL injection vulnerabilities. It allows users to:

- Discover database names, table names, columns, and their values from vulnerable web applications.
- Interact with the found data by switching between tables, columns, and values.
- Utilize SQL injection techniques to retrieve sensitive data through crafted HTTP requests.

**Note:** Time-based detection has been implemented, but the exploitation logic for time-based SQL injection is still under development. Contributions are welcome to complete this feature.

## Prerequisites

Before running the program, ensure that you have Python and the required dependencies installed.

### Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should include the following packages:

```
pip~=23.3.2
filelock~=3.13.1
certifi~=2024.8.30
urllib3~=2.2.3
idna~=3.10
requests~=2.32.3
```

## Usage

After installing the required dependencies, you can run the program using the following command in the main directory of the project:

```bash
python main.py "urlToTest"
```

Replace `"urlToTest"` with the target URL you wish to test for SQL injection vulnerabilities.

## Features

- **Boolean-based SQL Injection:** Exploits Boolean-based vulnerabilities to find the database name, table count, table names, column names, and their values.
- **Time-based SQL Injection Detection:** The program detects time-based vulnerabilities. However, the exploitation logic for time-based injections is not yet implemented. Users are encouraged to contribute to this feature.
- **Dynamic Exploration:** Allows the user to interactively explore discovered tables, columns, and values. The user can switch between tables and columns without restarting the program.

## Example Flow

1. **Start the exploitation process:**
   - The program first attempts to find the database name by exploiting a Boolean-based SQL injection vulnerability.
2. **Find tables and columns:**
   - Once the database name is discovered, the program will find tables and columns.
3. **Switch between tables and columns:**
   - Users can switch between discovered tables and columns to find specific data values.
4. **Display found data:**
   - The program displays the discovered data, including tables, columns, and values.

## Contribution

If you would like to contribute to the development of this tool, especially the time-based SQL injection exploitation feature, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.
