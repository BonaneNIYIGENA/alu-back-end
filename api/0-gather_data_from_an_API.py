#!/usr/bin/python3
"""
Export to CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    
    # Get user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')
    
    # Get todos data
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Write to CSV
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])