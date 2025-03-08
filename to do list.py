def main():
    task=[]
    while True:
        print("\n======== to do list ========")
        print("1. add task")
        print("2. show tasks")
        print("3. mark task as done")
        print("4 exit")

        choice = input("enter your choice")
        if choice == '1':
            print()
            n_task= int(input("how many task you want to add:"))
            for i in range(n_task):
                task=input("enter the task :")
                tasks.append({"task": task ,"done": False})
                print("task added")
        elif choice == '2':
            print("\ntask: ")
            for index, task in enumeratee(task):
                status="done" if task["done"] else "not done"
                print("{index + 1}.{task['task']}-{'status'}")
        elif choice_== '3':
            task_index= int(input("enter the task number to mark as done:"))-1
            if 0 <=task_index < len(task):
                tasks[task_index] ["done"] =True
                print("task marked as done :")
            else:
                print("invalid task number")
        elif choice== '4':
            print("exiting the to do list")
            break
        else:
            print("invalid choice. please try again")
if __name__=="__main__":
    main()
