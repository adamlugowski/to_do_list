task_id_counter = 1


def main():
    global task_id_counter
    tasks = {}
    print('''Welcome to the To-Do List App!
    --------------------------------
    1. Add a task
    2. View tasks
    3. Delete a task
    4. Mark task as complete
    5. Exit
    --------------------------------''')
    while True:
        try:
            user = int(input('Enter your choice: '))
            if user not in [1, 2, 3, 4, 5]:
                print('Type number in range 1-5: ')
                continue
        except ValueError:
            print('Input should be number. ')
            continue

        # Add a task
        if user == 1:
            task_description = input('Enter task description: ')
            tasks[task_id_counter] = {"description": task_description, "completed": False}
            print(f"Task '{task_description}' added with ID: {task_id_counter}.")
            task_id_counter += 1
        # View tasks
        elif user == 2:
            if not tasks:
                print('To do list is empty. ')
            else:
                for task_id, task_info in tasks.items():
                    status = 'Complete' if task_info['completed'] else 'Incomplete'
                    print(f"ID: {task_id} | Description: {task_info['description']} | Status: {status}. ")
        # Delete task
        elif user == 3:
            if not tasks:
                print('No tasks to delete. ')
            else:
                try:
                    task_id = int(input('Choose task ID to delete: '))
                    if task_id in tasks:
                        del tasks[task_id]
                        print(f"Task with ID {task_id} has been deleted. ")
                    else:
                        print('Task ID not found. ')
                except ValueError:
                    print('Enter a valid task ID (integer). ')
        # Mark a task as complete
        elif user == 4:
            if not tasks:
                print('No tasks available to mark as complete. ')
            else:
                try:
                    mark = int(input('Enter task ID to mark as complete: '))
                    if mark in tasks:
                        tasks[mark]['completed'] = True
                        print(f"Task with ID {mark} marked as complete. ")
                    else:
                        print('Task ID not found. ')
                except ValueError:
                    print('enter a valid task ID (integer). ')
        # Exit the application
        else:
            print('Exiting the application. ')
            break


if __name__ == '__main__':
    main()
