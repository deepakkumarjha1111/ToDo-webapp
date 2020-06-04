# ToDo-webapp
This is a web app made for a hackerearth hackathon.

OBJECTIVE:
To develop a pseudo Full Stack Web Application for Task Management To-do List.
You can use this To-do  app to make shopping lists or task lists, or take notes to increase your productivity and focus on what matters to you.
You can also set due date until when you have to complete that task.
From grocery lists to housecleaning routines, daily tasks are simple with To Do.
This To Do App is modern, easy-to-use experience makes your lists unique.


* Admin use cases:
-Admin can use this make  task available to his users and the have a track of the users of his tasks and the status of the users of his ongoing task.
-he can make the due dates for his specific tasks and can have an update of that tasks with this supporting app.
-Users with the successful completion of the admin task can update them at earliest with the status of the task. 

* Single user use cases:
-If a user want to mention his own task he can do this with the due date for his own task and can mark the respective status of his task status.
-He can also use this to help the different admins for their completion of the task with the eye on the mentioned due date .
-He can use the “USER” page for the direct updates of the mentioned tasks.


WORKING:
It uses FLASK framework to implement this website and the database is setup to save all the tasks and their due dates to the sqlite database.
The username and their credentials are saved again to the database of the sqlite database.   
The tasks which has been completed that can be mentioned to as TASK-COMPLETED to this shown webpage to have an idea about the tasks which are complete now and the user can proceed to the other task.
And lastly their is an implementation of an API.     
API  is helpful to store the user and their tasks status details in the database and the results are shown in the JSON format if it is tried to visualize.  

