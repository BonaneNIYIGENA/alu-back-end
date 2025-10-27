#!/usr/bin/python3
"""
This module uses the JSONPlaceholder REST API to retrieve information
about an employee's TODO list and export it to a CSV file.

The CSV file is named using the employee's ID and contains all tasks
owned by that employee in the format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Usage:
    ./1-export_to_CSV.py <employee_id>

Example:
    ./1-export_to_CSV.py 2
    # creates file '2.csv'
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_response.raise_for_status()
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch user's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Write CSV file named <USER_ID>.csv
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])