tasks=[]

print("\n=======Task flow menu========")
print("1.add task")
print("2.view tasks")
print("3.delete tasks")
print("exit")
while True:
    
    choice=input("enter your choice:")
    if choice=="1":
        while True:
            task=input("enter task:")
            if task.strip()== "":
                print(" task cannot be empty")
            else:
                 tasks.append(task)
                 print("task added sucessfully")
                 more=input("do you want to add more tasks?(yes\no:")
                 if more=="no":
                     break

    elif choice=="2":
        if len(task)==0:
            print("no task avaiable")
        else:
            print("\nyour tasks:")
            for i in range(len(tasks)):
                  print(i+1,tasks[i])
    elif choice=="3":
        if len(tasks)==0:
            print("no tasks to delete")
        else:
            try:
                num=int(input("enter task number to delete:"))
                if 1<=num<=len(tasks):
                    removed=tasks.pop(num-1)
                    print("deleted:",removed)

                else:
                    print("invalid number")
            except:
                print("enter a valid number")
    elif choice=="4":
        print("exiting taskflow...")
        break
    else:
        print("invalid choice")















