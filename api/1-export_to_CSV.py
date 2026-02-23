#!/usr/bin/python3
"""
Export an employee TODO list to CSV.
"""

import csv
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

    user_id = user.get("id")
    username = user.get("username")
    filename = "{}.csv".format(user_id)
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow(
                [user_id, username, task.get("completed"), task.get("title")]
            )


if __name__ == "__main__":
    main()
