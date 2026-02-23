#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import json
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
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {user_id: tasks}

    with open(f"{user_id}.json", mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
