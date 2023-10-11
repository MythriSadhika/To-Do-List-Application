# Initialize an empty dictionary to store tasks
tasks = {}

# Function to add a new task
def add_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter a description for the task: ")
    tasks[task_name] = task_description
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for task_name, task_description in tasks.items():
            print(f"Task: {task_name}\nDescription: {task_description}\n")

# Function to update a task
def update_task():
    view_tasks()
    task_name = input("Enter the name of the task to update: ")
    if task_name in tasks:
        new_description = input("Enter the updated description: ")
        tasks[task_name] = new_description
        print("Task updated successfully!")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_name = input("Enter the name of the task to delete: ")
    if task_name in tasks:
        del tasks[task_name]
        print("Task deleted successfully!")
    else:
        print("Task not found.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
