import process

print("\nTO-DO ORGANIZER!")

while True:
    choice = process.Account()
    if choice == 1:
        isLoggedIn = process.login()
        while isLoggedIn:
            if process.sizeOfList() == 0:
                while True:
                    try:
                        more = int(input("\nDo you want to add task? \n1.[YES]   2.[NO]\n-> "))
                        if more == 1:
                            process.AddTask()
                        elif more == 2:
                            break
                        elif more > 2 or more < 1:
                            print("\n\"Invalid Input!\"")
                    except Exception:
                        print("\n\"Something Went Wrong!\"")
            while True:
                process.show()
                choice = process.option()
                if choice == 1:
                    try:
                        editTask = int(input("\n1. Add a Task\n2. Re-Write a Task\n3. Remove a Task\n-> "))
                        if editTask == 1:
                            process.AddTask()
                        elif editTask == 2:
                            process.reWriteTask()
                        elif editTask == 3:
                            process.deleteTask()
                        elif editTask > 3:
                            print("\n\"Invalid Input\"")
                        else:
                            pass
                    except Exception:
                        print("\n\"Something Went Wrong!\"")
                elif choice == 2:
                        process.AddInProgress()
                elif choice == 3:
                        process.AddDone()
                elif choice == 4:
                        process.showInfo()
                elif choice == 0:
                    exit()
                    break
                elif choice > 4:
                    print("\n\"Invalid Input\"")
                else:
                    pass
    elif choice == 2:
        process.register()
    elif choice == 0:
        break
    elif choice > 2:
        print("\n\"Invalid Input\"")
    else:
        pass
