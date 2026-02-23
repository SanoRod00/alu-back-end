#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress.
"""

import requests
import sys


def main():
    """Script entry point."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/users/{}/todos".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
    except requests.RequestException:
        return

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return

    user = user_response.json()
    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get("completed") is True]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(done_tasks), len(todos)
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
