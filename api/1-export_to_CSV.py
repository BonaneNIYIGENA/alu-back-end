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
    
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")
    
    # Fetch todos data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()
    
    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])