import json
import argparse
import datetime as dt


#Setting up DateTime variable
now = dt.datetime.now()
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

#Loading data from JSON into the data variable
def load_tasks():
    try:
        with open("tasks.json") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []

#Appending new data into the JSON file
def save_tasks(new_item):
    tasks = load_tasks()
    tasks.append(new_item)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2) 


#Main Function
def main():
#Setup
    parser = argparse.ArgumentParser(description="A CLI for Task Management")
    subparser = parser.add_subparsers(dest="command")
#Add
    add_parser = subparser.add_parser("add", help='Adds tasks by typing: python main.py add')
#List
    list_parser = subparser.add_parser("list", help='List all tasks by typing: python main.py list')
#Delete
    delete_parser = subparser.add_parser("delete", help='Delete tasks by typing: python main.py delete ID#')
    delete_parser.add_argument('id', type=int)
#Update
    update_parser = subparser.add_parser('update', help= 'Update status of tasks by typing: python main.py update ID#')
    update_parser.add_argument('id', type=int)
#List Done
    list_done_parser = subparser.add_parser('list_done', help='List all tasks by typing: python main.py list_done')
#List In-Progress
    list_progress_parser = subparser.add_parser('list_inprogress', help='List all tasks by typing: python main.py list_inprogress')
#List Todo
    list_todo_parser = subparser.add_parser("list_todo", help='List all tasks by typing: python main.py list_todo')
#Setting args variable in order to read arguments
    args = parser.parse_args()


#ADD TASKS
    if args.command == "add":
        description = input("What is the task: ")
        tasks = load_tasks()
        max_id = max((item['id'] for item in tasks), default=0)   

        new_item = {
            "id": max_id + 1,
            "description": description,
            "status": "To-do",
            "created at": formatted_date,
            "updated at": formatted_date
        }
        save_tasks(new_item)
#LIST TASKS
    elif args.command == "list":
        tasks = load_tasks()
        for i in tasks:
            print(f"ID: {i["id"]}")
            print(f"Description: {i["description"]}")
            print(f"Status: {i["status"]}")
            print(f"Created: {i["created at"]}")
            print(f"Last Updated: {i["updated at"]}")
            print("-" * 30)

#DELETE TASKS
    elif args.command == "delete":
        new_list = []
        tasks = load_tasks()
        for i in tasks:
            if i["id"] != args.id:
                new_list.append(i)
            with open("tasks.json", "w") as f:
                json.dump(new_list, f, indent=2)

#UPDATE TASKS
    elif args.command == "update":
        #Getting inputs to find out what the description is and status, if they enter wrong they get an error message
        new_status = input("Is the task complete? (y/n): ")
        if new_status.lower() == "y":
            new_status = "Done"
        elif new_status.lower() == "n":
            new_status = input("Is the task in-progress? (y/n): ")
            if new_status.lower() == "y":
                new_status = "In-Progress"
            elif new_status.lower() == "n":
                new_status = "To-do"
            else: print("Invalid arguments input. Please try again.")
        else: print("Invalid arguments input. Please try again.")

        tasks = load_tasks()
        new_list = []
        for i in tasks:
            if i["id"] != args.id:
                new_list.append(i)
            else:
                new_item = {
                    "id": args.id,
                    "description": i["description"],
                    "status": new_status,
                    "created at": i["created at"],
                    "updated at": formatted_date
                }
                new_list.append(new_item)
        with open("tasks.json", "w") as f:
            json.dump(new_list, f, indent=2)

#LIST DONE TASKS
    elif args.command == "list_done":
        tasks = load_tasks()
        for i in tasks:
            if i["status"] == "Done":
                print(f"ID: {i["id"]}")
                print(f"Description: {i["description"]}")
                print(f"Status: {i["status"]}")
                print(f"Created: {i["created at"]}")
                print(f"Last Updated: {i["updated at"]}")
                print("-" * 30)

#LIST IN-PROGRESS
    elif args.command == "list_inprogress":
        tasks = load_tasks()
        for i in tasks:
            if i["status"] == "In-Progress":
                print(f"ID: {i["id"]}")
                print(f"Description: {i["description"]}")
                print(f"Status: {i["status"]}")
                print(f"Created: {i["created at"]}")
                print(f"Last Updated: {i["updated at"]}")
                print("-" * 30)

#LIST TO-DO     
    elif args.command == "list_todo":
        tasks = load_tasks()
        for i in tasks:
            if i["status"] == "To-do":
                print(f"ID: {i["id"]}")
                print(f"Description: {i["description"]}")
                print(f"Status: {i["status"]}")
                print(f"Created: {i["created at"]}")
                print(f"Last Updated: {i["updated at"]}")
                print("-" * 30)
    elif args.command is None:
        print(parser.print_help())


if __name__ == "__main__":
    main()