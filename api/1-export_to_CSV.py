#!/usr/bin/env python3
"""
Export to CSV format
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports employee TODO data to CSV format
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get('username')
    
    # Get employee's todos
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    
    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                str(task.get('completed')),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)