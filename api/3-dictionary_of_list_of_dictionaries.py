#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import json
import requests


def main():
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{base_url}/users").json()
    all_tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        all_tasks[user_id] = []
        username = user.get("username")

        todos = requests.get(f"{base_url}/users/{user_id}/todos").json()
        for task in todos:
            all_tasks[user_id].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    filename = "todo_all_employees.json"

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
