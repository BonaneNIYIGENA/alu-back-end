#!/usr/bin/python3
"""Export employee's TODO list to CSV"""

import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

user_id = sys.argv[1]

# Get user info
user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
if user_response.status_code != 200:
    print("Error: User not found")
    sys.exit(1)

user = user_response.json()
username = user.get("username")

# Get user's TODOs
todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
todos = todos_response.json()

# Write to CSV
csv_filename = f"{user_id}.csv"
with open(csv_filename, mode="w", newline='') as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])
