f=open("tasks.txt","a")
tasks=[]
print("Welcome to the To-Do List App!")
print("You can add tasks, view tasks, delete tasks or exit the app.")
print("1. Add a task")
print("2. View tasks")
print("3. Delete a task")
print("4. Exit")
while True:
    a=int(input("Enter your choice: "))
    if a==1:
        task=input("Enter the task you want to add: ")
        tasks.append(task)
        with open("tasks.txt","a") as f:
            f.write(task+"\n")
            print("Task added successfully!")
    elif a==2:
        print("Your tasks are:")
        for i in range(0,len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    elif a==3:
        task=input("Enter the task you want to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found in the list.")
    elif a==4:
        print("Exiting the app. Goodbye!")
        break

f.close()