#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_data = requests.get(url + f"users/{user_id}").json()
    username = user_data["username"]

    # Fetch todos
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Prepare data for CSV export
    csv_data = []
    for task in todos:
        task_status = "Completed" if task["completed"] else "Not Completed"
        task_title = task["title"]
        csv_data.append([user_id, username, task_status, task_title])

    # Export data to CSV
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)
