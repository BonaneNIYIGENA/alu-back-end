#!/usr/bin/python3
"""
Script that exports employee TODO list data to CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Write to CSV file
    filename = "{}.csv".format(user_id)
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                str(user_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])