#!/usr/bin/python3
"""
Python script that, using this REST API, for
a given employee ID, returns information about
his/her TODO list progress.
"""
import json
import requests


def main():
    """main method"""
    user_id = [i for i in range(1, 11)]
    url = "https://jsonplaceholder.typicode.com/users"
    all_user = [username['username'] for username in requests.get(url).json()]
    data = {}
    for i in range(10):
        user_url = url + "/{}".format(user_id[i])
        task_url = user_url + "/todos"
        dict_data = []
        response_task = requests.get(task_url).json()
        for task in response_task:
            inner_dict = {}
            inner_dict["username"] = all_user[i]
            inner_dict["task"] = task["title"]
            inner_dict["completed"] = task["completed"]
            dict_data.append(inner_dict)
        data[user_id[i]] = dict_data
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    main()
