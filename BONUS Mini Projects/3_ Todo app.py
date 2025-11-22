print("Welcome to the Todo App!")
dos=[]
print("1. Add a task \n2. Delete task \n3. View all tasks \n4. Exit")
while True:
    opt=int(input("Chose an option: "))
    if opt==1:
        task=input("Enter the task: ")
        dos.append(task)
        print("Task added successfully!")
    elif opt==2:
        task=input("Enter the task to be deleted: ")
        if task in dos:
            dos.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task no found!")
    elif opt==3:
        print("your tasks are: ")
        print(type(dos))
        for i in dos:
            print(i)
    elif opt==4:
        break
    else:
        print("Invalid option! Please try again.")