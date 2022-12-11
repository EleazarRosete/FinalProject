# **To-Do Organizer**

- ### This system is about organizing task that you want to do. You will earn points just by doing the task. Who knows, maybe you can climb your ranked too.

> ## **Main.py**

- #### will get manipulate all the functions needed to run the system

> ## **Process.py**

- #### Have all the functions that manipulate the data/value from the user 

> ## **Person.py**

- #### Holds the User's username and password as well as displaying the user's stats like user name, user password, user points, user ranks and the task's done.

> ## **Instructions**
  1. sign in
  2. register
     exit

-Select Register to make an account if you don't have one.
-Select Sign in if you'd already have an account.

  The system will ask you if you want to add task or not
  -yes
  -no
  
  if you choose "No", An overview of the system will showup with different option to choose.
  if you choose "Yes", An overview will also showup but, it will show the task you input. 
  
      
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
