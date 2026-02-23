#!/usr/bin/python3
"""Export an employee TODO list to CSV."""

import csv
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{base_url}/users/{user_id}/todos").json()

    with open(f"{user_id}.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])


if __name__ == "__main__":
    main()
