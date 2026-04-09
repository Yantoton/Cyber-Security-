todo_list = []
while True:
    banner = "Welcome to t(o_d)o list:"
    print(banner)
    choice = input("Would you like to add a task?(yes/no)")

    if choice == "yes":
        add_task = input("write here to add a task:")
        todo_list.append(add_task)
        print(f"Task {add_task} added successfully:" )

    elif choice == "no":
        print("Here your task list is:",todo_list)
        break

    else:
        print("please enter yes or no")
