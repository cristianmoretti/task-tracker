import os 
import textwrap 
from datetime import datetime 
import json 
import pandas as pd 

#check if task folder exists 
def check_for_folder(): 
    dir_list = os.listdir()
    if "task" in dir_list: 
        print("Task folder already in project directory")
        return True 
    else:
        return False 
    
#create folder if not exists 
def create_folder(): 
    if not check_for_folder(): 
        os.mkdir("task")
    else: 
        return 

#check if json exist in task folder 
def check_for_json(): 
    if "task.json" in os.listdir("task"): 
        return True
    else: 
        return False 

#create json if not exists 
def creare_json():  
    if not check_for_json():
        with open("task/task.json", "w") as f:
            f.write(textwrap.dedent(
                """
                    {
                        "task": []
                    }
                """)
            )

#add task to json 
def add_task(): 
    task = input("Enter task name here: ")
    status = input("Enter task status here (complete/pending/in progress): ")
    creation_time = datetime.now().strftime("%Y-%m-%d")
    modified_time = "" 

    with open("task/task.json", "r") as f:
        data = json.load(f) 

    data["task"].append({
        "task": task,
        "status": status,
        "creation_time": creation_time,
        "modified_time": modified_time
    })

    with open("task/task.json", "w") as f:
        json.dump(data, f, indent=4)

#delete task from json 
def delete_task(): 
    task = input("Enter task name to delete: ")
    with open("task/task.json", "r") as f:
        data = json.load(f)

    available_tasks = data["task"]
    for task_item in available_tasks: 
        if task_item["task"] == task:
            available_tasks.remove(task_item)
            break

    with open("task/task.json", "w") as f: 
        json.dump(data, f, indent=4)

#update task in json 
def update_task(): 
    task = input("Enter task name to update: ")
    with open("task/task.json", "r") as f: 
        data = json.load(f)

    available_tasks = data["task"]
    for task_item in available_tasks: 
        if task_item["task"]  == task: 
            new_status = input(f"Entrer the new status for {task} (complete/pending/in progress): ")  
            task_item["status"] = new_status
            task_item["modified_time"] = datetime.now().strftime("%Y-%m-%d")
            break

    with open("task/task.json", "w") as f: 
        json.dump(data, f, indent=4)

#show data 
def show_data(): 
    with open("task/task.json", "r") as f: 
        data = json.load(f) 

    df = pd.DataFrame(data["task"])
    print(df)


def user_action(): 
    action = input("Enter action to perform (add/delete/update/show): ")
    if action == 'add': 
        add_task() 
    elif action == 'delete': 
        delete_task()
    elif action == 'update': 
        update_task()
    elif action == 'show': 
        show_data()
    else: 
        print(f"Invalid action: {action}")

#main orchestrator
def main():
    create_folder()
    creare_json()
    user_action()

if __name__ == "__main__":
    main() 