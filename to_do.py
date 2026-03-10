class TodoList:
    def __init__(self):
        self.task_lst = []
    
    def add_task(self): 
        self.task = input("enter task: ").split(",")
        for task in self.task:
            self.task_lst.append(task)
        print("task added successfully!")
    
    def view_task(self):
        if len(self.task_lst) == 0:
            print("No tasks available")
        else:
            print("Your tasks: ")
            for i , task in enumerate(self.task_lst,1):
                print(f"{i}.{task}")
    
    def delete_task(self):
        self.view_task()
        
        try:
            num = int(input("enter any number: "))
            if 0 < num <= len(self.task_lst):
                removed = self.task_lst.pop(num-1)
                print("Deleted:",removed)
            else:
                print("invalid task num")
        except ValueError:
            print("Invalid value")
user1 = TodoList()    

while True:
        
    print("\n1 for Add task")
    print("2 for View task")
    print("3 for Delete task")
    print("4 for Exit")

    choice = int(input("enter choice: "))

    if choice == 1:
        user1.add_task()
    elif choice == 2:
        user1.view_task()
    elif choice == 3:
        user1.delete_task()
    elif choice == 4:
        print("Thanks for using!")
        break
    else:
        print("It's out of range")
    

