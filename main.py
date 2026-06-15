tasks = []

while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        task = input("Enter New Task: ")
        tasks.append(task)

        print("Task Added Successfully")

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Found")

        else:
            print("\nYour Tasks:")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks Available")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            delete = int(input("Enter Task Number: "))

            if 1 <= delete <= len(tasks):
                tasks.pop(delete - 1)
                print("Task Deleted Successfully")
            else:
                print("Invalid Number")

    elif choice == "4":

        print("Thank You")
        break

    else:

        print("Invalid Choice")