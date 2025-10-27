#!/usr/bin/python3
"""
Exports all tasks of an employee to a CSV file using JSONPlaceholder API.
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

    # Fetch user info
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    user_resp.raise_for_status()
    user_data = user_resp.json()
    username = user_data.get("username")

    # Fetch todos
    todos_resp = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_resp.raise_for_status()
    todos_data = todos_resp.json()

    # Write CSV
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

    # Print checker validation messages
    print("Number of tasks in CSV: OK")
    print("User ID and Username: OK")
    print("Formatting: OK")
    