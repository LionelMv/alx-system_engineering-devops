#!/usr/bin/python3
"""
Request from API; Return TODO list progress of all employees
Export this data to JSON
"""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    all_users = requests.get(url + "users").json()

    data = {
        user["id"]: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in requests.get(url + "todos",
                                     params={"userId": user["id"]}).json()
            ] for user in all_users
        }

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
