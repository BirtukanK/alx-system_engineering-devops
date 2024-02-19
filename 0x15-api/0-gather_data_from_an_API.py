#!/usr/bin/python3
""" Defines a python script to acess REST API"""
import requests
import sys

url = "https://jsonplaceholder.typicode.com"
employee_id = int(sys.argv[1])

user_response = requests.get(f"{url}/users/{employee_id}")
todos_response = requests.get(f"{url}/todos?userId={employee_id}")

user_data = user_response.json()
todos_data = todos_response.json()
employee_name = user_data.get("name")

completed_tasks = [task for task in todos_data if task["completed"]]
number_of_done_tasks = len(completed_tasks)
total_number_of_tasks = len(todos_data)

print(f"Employee {employee_name} is done with tasks
      ({number_of_done_tasks}/{total_number_of_tasks}): ")
for task in completed_tasks:
    print(f"\t{task['title']}")
