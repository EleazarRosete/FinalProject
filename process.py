import person


# Account {
def Account():
    choice = int(input("\n1. Sign In\n2. Register\n0. Exit\n-> "))
    return choice


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
# }


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
        print("\nNo Task Done Yet!\n")


# Organizer {
def option():
    choice = int(input("================================================\nOptions:\n1. Add Task\n2. Do Task\n3. "
                       "Finished Tasks\n4. Show User Info\n0. Exit\n-> "))
    return choice


def show():
    # TO DO
    ctr = 1
    print(
        "\n================================================\n--------------------Overview--------------------\n================================================")
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
    return task


# Organizer -> Add Task -> Edit Task
def reWriteTask():
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ". " + x)
            ctr += 1
        ctr = 1
        edit = int(input("\nEnter the task number you want to edit: "))
        if edit > len(task):
            print("\nInvalid Input!\n")
        elif edit < 0:
            print("\nInvalid Input!\n")
        else:
            edit -= 1
            task[edit] = input("Enter new task: ")
    else:
        print("\"No Task to Edit\"")


# Organizer -> Add Task-> Delete Task
def deleteTask():
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ". " + x)
            ctr += 1
        ctr = 1
        delete = int(input("\nEnter the task number you want to remove: "))
        if delete > len(task):
            print("\nInvalid Input!\n")
        elif delete < 0:
            print("\nInvalid Input!\n")
        else:
            delete -= 1
            task.pop(delete)
    else:
        print("No Task to Remove")


# Organizer -> In Progress
def AddInProgress():
    if len(task) != 0:
        ctr = 1
        for x in task:
            print(ctr, ".", x)
            ctr += 1
        ctr = 1
        index = int(input("Enter the task number you want to do: "))
        if index > len(task):
            print("\nInvalid Input!\n")
        elif index < 0:
            print("\nInvalid Input!\n")
        else:
            index -= 1
            inProgress.append(task[index])
            task.pop(index)
    else:
        print("No Task to Add in Progress")


# Organizer -> Remove Task
def AddDone():
    if len(inProgress) != 0:
        ctr = 1
        for x in inProgress:
            print(ctr, ".", x)
            ctr += 1
        ctr = 1
        index = int(input("Enter the task number you already did: "))
        print(index)
        if index > len(inProgress):
            print("\nInvalid Input!\n")
        elif index < 0:
            print("\nInvalid Input!\n")
        else:
            index -= 1
            done.append(inProgress[index])
            inProgress.pop(index)
            global totalPoints
            totalPoints = totalPoints + 250
            Rank(totalPoints)

    else:
        print("No Progress to Add in Done")
# }


task = list()
inProgress = list()
done = list()
usernames = list()
passwords = list()
User = ""
Pass = ""
rank = ""
totalPoints = 0
