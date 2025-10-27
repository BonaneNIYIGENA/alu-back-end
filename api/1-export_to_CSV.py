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
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch user's todo list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # File name is <employee_id>.csv
    filename = f"{employee_id}.csv"

    # Write CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])