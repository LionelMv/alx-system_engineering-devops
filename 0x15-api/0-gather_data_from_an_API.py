#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests
from sys import argv

if __name__ == '__main__':
    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_data = requests.get(url + f"users/{user_id}").json()
    employee_name = user_data["name"]

    # Fetch todos
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t{task}")
