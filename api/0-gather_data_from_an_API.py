#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed = [t for t in todos if t.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todos)))

    for task in completed:
        print("\t{}".format(task.get('title')))


if __name__ == '__main__':
    main()
