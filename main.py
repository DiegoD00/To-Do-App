task = []
def todo_app():

    choice = ""
    try:
        f = open("task.txt")
        for i in f:
            task.append(i.strip())
        f.close()
    except:
        print("No existing tasks found.")
   
    while choice != "4":

        print("\n1. View tasks")
        print("\n2. Add a task")
        print("\n3. Delete a task")
        print("\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            print("Viewing tasks...")
            count = 1
            if len(task) == 0:
                print("No tasks available.")

            for i in task:
                print(f"{count}. {i}")
                count += 1
         
        elif choice == "2":
            print("Adding a task...")
            tasko = input("Enter the task: ")
            task.append(tasko)
            f = open("task.txt", "a")
            f.write(tasko + "\n")
            f.close()
        
                
                
        elif choice == "3":
            print("Deleting a task...")
            count = 1
            if len(task) == 0:
                print("No tasks available.")

            for i in task:
                print(f"{count}. {i}")
                count += 1
            
            try:
                index = int(input("Enter the number of the task to delete: "))
                if index not in range(1, len(task) + 1) or len(task) == 0:
                    print("Invalid task number. Please try again.")
                else:
                    del task[index - 1]
                    f = open("task.txt", "w")
                    for i in task:
                        f.write(i + "\n")
                    f.close()
            except:
                print("Incorrect input, please enter a valid number.")

           

        elif choice == "4":
            print("Exiting the application. Goodbye!")
        
        else:
            print("Invalid option. Please try again.")
            
            
        
       
            
        
            
todo_app()

