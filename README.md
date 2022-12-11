# **To-Do Organizer**

- ### This system is about organizing task that you want to do. You will earn points just by doing the task. Who knows, maybe you can climb your ranked too.

> ## **Main.py**

- #### will get and manipulate all the functions needed to run the system

> ## **Process.py**

- #### Have all the functions that manipulate the data/value from the user 

> ## **Person.py**

- #### Holds the User's username and password as well as displaying the user's stats like user name, user password, user points, user ranks and the task's done.

> ## **Instructions**
- 1. sign in
  2. register
  0. exit
  -"you'll decide what do u want to print."
    if 1 an error will occur because you don't have any account yet.
    2. register
      1. enter username
      2. enter password
   -"Since you typed your desired username and password, your account is finally created."
   1. sign in
      1. enter username
      2. enter password
      - after inputing correct username it will ask you if you want to add task or not.
      
- ### [**To-Do Organizer Video Presentation**](https://youtu.be/dp9IYkGYEF0)

- ### **UML Diagram**
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

> ## **Contributors**

| Name | Contibutions |
|:---| :---|
| Eleazar Rosete | Create Code |
| Errol Villanueva | Polish Codes |
| Mykel Cruz | Polish Codes |
| Ivan Ebora | Polish Codes |
