"""
A simple command-line task management application that allows users to add tasks,
view their task list, and mark them as complete.

To run the app, use the below command:
python3 run.py
"""


def display_menu():
    """
    Displays the main menu options for the to-do list app.
    """
    print("\nTo-Do List Application")
    print("----------------------")
    print("1. View To-Do List")
    print("2. Add a New Task")
    print("3. Complete a Task")
    print("4. Exit")
    print("----------------------")


def view_tasks(todo_list):
    """
    Displays the tasks in the to-do list.

    :param todo_list: List of dictionaries containing task info.
    """
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index}. {task['name']} - {status}")


def add_task(todo_list):
    """
    Adds a new task to the to-do list.

    :param todo_list: List of dictionaries containing task info.
    """
    task_name = input("Enter the name of the new task:\n").strip()
    if task_name:
        todo_list.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added to the list.")
    else:
        print("Task name cannot be empty.")


def complete_task(todo_list):
    """
    Marks a task as completed in the to-do list.

    :param todo_list: List of dictionaries containing task info.
    """
    view_tasks(todo_list)
    try:
        task_number = int(input("Enter the task number you've completed:\n"))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print(f"Task '{todo_list[task_number - 1]['name']}' marked done.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """
    The main function that runs the to-do list app.
    """
    todo_list = []  # Initialize an empty to-do list

    while True:
        display_menu()
        choice = input("Choose an option:\n").strip()

        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
