import process

print("\nTo-Do Organizer!\n")

while True:
    choice = process.Account()
    match choice:
        case 1:
            isLoggedIn = process.login()
            while isLoggedIn:
                if process.sizeOfList() == 0:
                    while True:
                        todo = process.AddTask()
                        more = int(input("Do you want to add more task? \n1.[YES]   2.[NO]\n-> "))
                        if more == 2:
                            break
                while True:
                    process.show()
                    choice = process.option()
                    if choice == 1:
                        editTask = int(input("\n1. Add a Task\n2. Re-Write a Task\n3. Remove a Task\n-> "))
                        if editTask == 1:
                            process.AddTask()
                        elif editTask == 2:
                            process.reWriteTask()
                        elif editTask == 3:
                            process.deleteTask()
                        else:
                            print("\nInvalid Input\n")
                    elif choice == 2:
                        process.AddInProgress()
                    elif choice == 3:
                        process.AddDone()
                    elif choice == 4:
                        process.showInfo()
                    elif choice == 0:
                        exit()
                        break
                    else:
                        print("\nINVALID\n")
        case 2:
            process.register()
        case 0:
            break
        case _:
            print("Invalid Input")
