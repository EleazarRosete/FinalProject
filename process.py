import person


# Account {
def Account():
    try:
        choice = int(input("\n1. Sign In\n2. Register\n0. Exit\n-> "))
        return choice
    except Exception:
        print("\n\"Something Went Wrong!\"")
        return -1


def login():
    if len(usernames) != 0 and len(passwords) != 0:
        isUserTrue = False
        isPassTrue = False
        global User
        User = input("\nEnter your username: ")
        global Pass
        Pass = input("Enter your password: ")
        for x in usernames:
            if x == User:
                isUserTrue = True
        for x in passwords:
            if x == Pass:
                isPassTrue = True
        if isUserTrue == True and isPassTrue == True:
            print("\n\"Logged In Successfully!\"")
            return True
        else:
            print("\n\"Incorrect username or password!\"")
            return False
    else:
        print("\nNo Account Yet!")


def register():
    setUsername = input("\nEnter a Username: ")
    setPassword = input("Enter a Password: ")
    person.user(setUsername, setPassword)
    usernames.append(setUsername)
    passwords.append(setPassword)


# Rank System
def Rank(points):
    global rank
    if points > 1000:
        rank = "Doctoral"
        return rank
    elif points > 500:
        rank = "Masteral"
        return rank
    elif points > 250:
        rank = "Bachelor"
        return rank
    else:
        rank = "Undergraduate"
        return rank


# Show Info
def showInfo():
    if len(done) != 0:
        person.stats(User, Pass, totalPoints, rank, done)
    else:
        person.stats(User, Pass, totalPoints, rank, "None")


# Organizer {
def option():
    try:
        choice = int(input("================================================\nOptions:\n1. Add Task\n2. Do Task\n3. "
                           "Finished Tasks\n4. Show User Info\n0. Exit\n-> "))
        return choice
    except Exception:
        print("\n\"Something Went Wrong!\"")
        return -1


def show():
    # TO DO
    ctr = 1
    print(
        "\n================================================\n--------------------Overview--------------------\n"
        "================================================")
    print("Tasks:")
    if len(task) == 0:
        print("\"There's no task available!\"")
    else:
        for x in task:
            print(ctr, ". " + x)
            ctr += 1
    # IN PROGRESS
    ctr = 1
    print("------------------------------------------------\nIn Progress:")
    if len(inProgress) == 0:
        print("\"There's no task in progress!\"")
    else:
        for x in inProgress:
            print(ctr, ". " + x)
            ctr += 1
    # FINISHED
    ctr = 1
    print("------------------------------------------------\nDone:")
    if len(done) == 0:
        print("\"You haven't done any task!\"")
    else:
        for x in done:
            print(ctr, ". " + x)
            ctr += 1
    ctr += 1


def sizeOfList():
    size = len(task)
    return size


# Organizer -> Add Task
def AddTask():  # list of task
    todo = input("\nAdd a Task: ")
    task.append(todo)
    print("\n\"Task Added!\"")
    return task


# Organizer -> Add Task -> Edit Task
def reWriteTask():
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ". " + x)
            ctr += 1
        ctr = 1
        try:
            edit = int(input("\nEnter the task number you want to edit: "))
            if edit > len(task):
                print("\n\"Invalid Input\"")
            elif edit < 0:
                print("\n\"Invalid Input\"")
            else:
                edit -= 1
                task[edit] = input("Enter new task: ")
        except Exception:
            print("\n\"Something Went Wrong!\"")
    else:
        print("\n\"No Task to Edit!\"")


# Organizer -> Add Task-> Delete Task
def deleteTask():
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ". " + x)
            ctr += 1
        ctr = 1
        try:
            delete = int(input("\nEnter the task number you want to remove: "))
            if delete > len(task):
                print("\n\"Invalid Input\"")
            elif delete < 0:
                print("\n\"Invalid Input\"")
            else:
                delete -= 1
                task.pop(delete)
        except Exception:
            print("\n\"Something Went Wrong!\"")
    else:
        print("\n\"No Task to Remove!\"")


# Organizer -> In Progress
def AddInProgress():
    print("----------------------Task----------------------")
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ".", x)
            ctr += 1
        ctr = 1
        try:
            index = int(input("Enter the task number you want to do: "))
            if index > len(task):
                print("\n\"Invalid Input\"")
            elif index < 0:
                print("\n\"Invalid Input\"")
            else:
                index -= 1
                inProgress.append(task[index])
                task.pop(index)
        except Exception:
            print("\n\"Something Went Wrong!\"")
    else:
        print("\"No Task to Add in Progress!\"")


# Organizer -> Remove Task
def AddDone():
    print("-------------------In Progress------------------")
    if len(inProgress) != 0:
        ctr = 1
        for x in inProgress:
            print(ctr, ".", x)
            ctr += 1
        ctr = 1
        try:
            index = int(input("Enter the task number you already did: "))
            print(index)
            if index > len(inProgress):
                print("\n\"Invalid Input\"")
            elif index < 0:
                print("\n\"Invalid Input\"")
            else:
                index -= 1
                done.append(inProgress[index])
                inProgress.pop(index)
                global totalPoints
                totalPoints = totalPoints + 250
                Rank(totalPoints)
        except Exception:
            print("\n\"Something Went Wrong!\"")
    else:
        print("\"No Progress to Add in Done!\"")



task = list()
inProgress = list()
done = list()
usernames = list()
passwords = list()
User = ""
Pass = ""
rank = ""
totalPoints = 0
