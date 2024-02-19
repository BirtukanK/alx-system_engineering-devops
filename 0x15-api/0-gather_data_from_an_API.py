#!/usr/bin/python3
""" Defines a python script to acess REST API
"""
import requests
import sys
""" all necessary modules imported"""

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user_response = requests.get(f"{url}/users/{employee_id}")
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()
    employee_name = user_data.get("name")

    completed_tasks = [task for task in todos_data if task["completed"]]
    done = len(completed_tasks)
    total = len(todos_data)

    print(f"Employee {employee_name} is done with tasks({done}/{total}):")
    for task in completed_tasks:
        print(f"     {task['title']}")
