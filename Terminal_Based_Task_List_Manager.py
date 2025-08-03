import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE,'r',encoding="utf-8") as file:
            for line in file:
                txt,status = line.strip().rsplit("||",1) # Splitting the string from right  
                tasks.append({"text":txt,"done": status == "done"}) # applying the condition inside the dictionary append the task if status is "done"
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE,"w",encoding="utf-8") as file:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            file.write(f"{task['text']}||{status}\n") # updating the status of the tasks 

def display_tasks(tasks):
    if not tasks:
        print(f"No Tasks found")
    else:
        for i,task in enumerate(tasks,1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}.[{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n---------Task List Manager----------")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text,"done":False})
                    save_tasks(tasks)
                else:
                    print("Task Cannot be empty")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number"))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(tasks)
                        print("task marked as Done")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete"))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting the task manager....")
                break
            case _: # if no value is given which means it scans for every alphabet or number 
                print("Please choose a valid option")


task_manager()



