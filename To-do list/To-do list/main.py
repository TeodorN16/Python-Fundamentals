tasks = []

while True:
    try:
        print("\nHello, how are you today?")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit the program")

        number = int(input("Choose an action: "))

        if number == 1:
            description = input("Describe the task: ")
            tasks.append({"desc": description, "completed": False})
            print("Successfully added task!")

        elif number == 2:
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"{i}. {task['desc']} [{status}]")

        elif number == 3:
            if not tasks:
                print("No tasks to mark as complete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"{i}. {task['desc']} [{status}]")

                task_num = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number!")

        elif number == 4:
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"{i}. {task['desc']} [{status}]")

                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    print(f"Deleted task: {deleted_task['desc']}")
                else:
                    print("Invalid task number!")

        elif number == 5:
            print("Goodbye!")
            break

        else:
            print("Please enter a number from 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter a number.")
