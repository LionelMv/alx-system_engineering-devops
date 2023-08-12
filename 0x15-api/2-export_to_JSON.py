#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to JSON
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_data = requests.get(url + f"users/{user_id}").json()
    employee_name = user_data["name"]
    username = user_data["username"]

    # Fetch todos
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    json_data = {user_id: [{"task": task["title"],
                            "completed": task["completed"],
                            "username": username} for task in todos]}

    file_name = f"{user_id}.json"
    with open(file_name, "w") as jsonfile:
        json.dump(json_data, jsonfile)
