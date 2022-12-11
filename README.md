# **To-Do Organizer**

- ### This system is about organizing task that you want to do. You will earn points just by doing the task. Who knows, maybe you can climb your ranked too.

> ## **Main.py**

- #### Will call and manipulate all the functions needed to run the system

> ## **Process.py**

- #### Have all the functions that manipulate the data/value from the user 

> ## **Person.py**

- #### Holds the User's username and password as well as displaying the user's stats like user name, user password, user points, user ranks and the task's done.


> ## **Instructions**

**TO-DO ORGANIZER!**

Starts by asking the user to Log in the system.

    - 1. Sign in
    - 2. Register
    - 0. Exit
- Select Register to make an account if you don't have one.

- Select Sign in if you'd already have an account.

The system will ask you if you want to add task or not.

    - Do you want to Add Task?
        - 1. Yes
        - 2. No
  
- If you choose "No", An overview of the system will showup with different option to choose.

- If you choose "Yes", you'll enter a task and the system will ask you again if you want to add task.

Then options will show to help you organize the task.

    - Options:
      - 1. Add Task
      - 2. Do Task
      - 3. Finished Task
      - 4. Show User Info
      - 0. Exit

- If you choose "Add Task" another options to choose whether you want to: 
    
        - 1. Add a Task
        - 2. Re-write a Task
        - 3. Remove a Task

    - If you choose "Add a Task", you will add more task.
    - If you choose "Re-write a Task", you will edit a certain task.
    - If you choose "Delete a Task", you will remove a certain task.

- If you choose "Do Task", you will choose a task in task list to do it.
- If you choose "Finished Task", you've finished the task and you want to put it in finished task to gain points and rank up from "Undergraduate to Doctoral".
- If you choose to "Show User Info", your username, password, gain points, current rank and accomplished task will be displayed.

- And, if you don't want to do or add task anymore you can just exit the program with ease.
      
> ## [**To-Do Organizer Video Presentation**](https://youtu.be/dp9IYkGYEF0)

> ## **UML Diagram**
| Main.py |...|
|:---|:--:|
|Variables| choice|
| Functions | calling functions from Process.py|

| Process.py |...|
|:---|:--:|
|Variables| task, inProgress, done, usernames, passwords, User, Pass, rank , totalPoints|
| Functions | Account(), login(), register(), Rank(), showInfo(), option(), show(), sizeOfList(), AddTask(), deleteTask(), AddInProgress(), AddDone()|

| Person.py |...|
|:---|:--:|
|Class| user, stats(user)|

> ## **Rating**

10/10 is the group rate not just by the group members but also some of our classmates. OOP is used in the system a lot of functions to run the system. The idea was so good and the system can helps a lot of people especially students and employers who find their self struggling in making a their works. 


> ## **Contributors**

| Name | Contibutions |
|:---| :---|
| Eleazar Rosete | Create Code |
| Errol Villanueva | Polish Codes |
| Mykel Cruz | Polish Codes |
| Ivan Ebora | Polish Codes |
