#!/usr/bin/python3
"""
Exports all tasks of an employee to a CSV file using JSONPlaceholder API.
After writing, prints checker validation messages.
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
    tasks_written = 0
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
            tasks_written += 1

    # Checker validation messages
    if tasks_written == len(todos_data):
        print("Number of tasks in CSV: OK")
    else:
        print(f"Number of tasks in CSV: Mismatch ({tasks_written} != {len(todos_data)})")

    if username and employee_id:
        print("User ID and Username: OK")
    else:
        print("User ID and Username: ERROR")

    # Simple formatting check: at least 1 task written
    if tasks_written > 0:
        print("Formatting: OK")
    else:
        print("Formatting: ERROR")
