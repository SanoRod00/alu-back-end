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
    todos = requests.get(f"{base_url}/todos").json()

    user_map = {}
    all_tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        user_map[user_id] = user.get("username")
        all_tasks[user_id] = []

    for task in todos:
        user_id = str(task.get("userId"))
        if user_id in all_tasks:
            all_tasks[user_id].append({
                "username": user_map[user_id],
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    filename = "todo_all_employees.json"

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
