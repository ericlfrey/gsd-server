# Get Shit Done -- Full Stack Version!
This is the server side portion of the full stack version of my Nashville Software School Front End Capstone: [Get Shit Done](https://github.com/ericlfrey/PROject-Planner)

![logo](https://user-images.githubusercontent.com/107942776/223236457-7dfa7824-1aa7-4609-9841-a8923173329d.png)

## Topics
- [Overview](#overview)
- [MVP Features](#mvp-features)
- [Try the App Yourself](#try-the-app-yourself)
- [Planning to Get Shit Done](#planning)
- [Code Snippets](#code-snippets)
- [Tech Stacks for Get Shit Done](#tech-stacks)
<!-- - [Stretch Features](#stretch-features) -->

## Overview
This is a Django server application built to provide the database for the [client-side app](https://github.com/ericlfrey/gsd-client)

Get Shit Done is a Project Planning App that allows a User to Create, Read, Update and Delete a Project, and then maintain full CRUD on  Tasks and Materials associated with the Project. 

Planning is hard. Maintaining details on several projects at once can easily lead to disorganization. GSD was designed to help organize details and maintain the scope of several projects at once, all in one place. Not only can Tasks be easily seen in the Project Details for initial planning and implementation, but also Materials are easliy assigned to Tasks, and also tallied up so the User can see the Estimated Cost of the Project.

## MVP Features 

<em>Projects:</em>
- Sign in via Google Authentication
- Add a new Project to see the project folder visible on the home page with all other open projects.
- Clicking the Project folder takes the User to the Project Details page which has the open Tasks and Materials associated with the Project. Also this page contains the Date Created, and Estimated Cost of the Project.
- The Actions dropdown has options for the User to Edit the Project Name, Delete the Project, Add a Task, or Add a Material.
- Deleting a Project also deletes all associated Tasks and Materials.
<img src="https://user-images.githubusercontent.com/107942776/223227346-583dd132-ffa5-40c7-8076-2e225b9100be.png" width="500"/>
<img src="https://user-images.githubusercontent.com/107942776/223227374-80f9f9b8-a9d6-4a50-9b90-cab5c87903d2.png" width="500"/>

<em>Tasks:</em>
- Task Cards on the Project Details page show the Status (not started, in progress, complete) an the Due Date.
- Clicking the dropdown has options for the User to view the Task Details page, Edit the Task, or Delete the Task.
- Clicking the Task Name also takes the User to the Task Details Page.
- The Task Details Page shows the associated Project, Date Created, Due Date, and the Task Details. 
- The dropdown has options for the User to Edit or Delete the Task.
<img src="https://user-images.githubusercontent.com/107942776/223227439-de198d43-2aa6-415a-a440-8a03bc217682.png" width="500"/>

<em>Materials:</em>
- Material Cards on the Project Details page show the Status (acquired, not acquired) and the associated Task.
- Clicking the dropdown has options for the User to view the Material Details page, Edit the Material, or Delete the Material.
- Clicking the Material Name also takes the User to the Material Details Page.
- The Material Details Page shows the Total Material Cost, associated Project and Task, Status, Price, and Quantity. 
- The dropdown has options for the User to Edit or Delete the Material.
<img src="https://user-images.githubusercontent.com/107942776/223227453-e2c94084-9572-49ae-b670-92d81d434963.png" width="500"/>


## Try the app yourself

1. Clone GSD to your local machine 
```
git clone git@github.com:ericlfrey/gsd-server.git
```
2. Move into the directory
```
cd gsd-server
```
3. Install pyenv * optional
```
pip install pyenv
```
4. Install Python [3.9.16](https://www.python.org/downloads/release/python-3916/)
5. Install pipenv
```
pip install pipenv
```
6. Start your virtual environment
```
pipenv shell
```
7. Run the Server
```
python3 manage.py runserver
```
8. Setup and run the [Get Shit Done Client](https://github.com/ericlfrey/gsd-client) for this project to run on local machine.



## Planning
#### ERD for GSD MVP
<img src="https://user-images.githubusercontent.com/107942776/242314139-52b847cf-59ab-4141-8fbc-331238e73f85.png" width="500"/>

[Link to ERD](https://dbdiagram.io/d/645d6fdddca9fb07c4f01fd6)


## Code Snippets

#### Task Model
<img src="https://user-images.githubusercontent.com/107942776/242320231-07026a20-b801-4819-ae3e-29df73477cec.png" width="500"/>

#### Material Model
<img src="https://user-images.githubusercontent.com/107942776/242320236-0839c03f-e505-408f-a31e-395de712425f.png" width="500"/>

#### Project List Method
<img src="https://user-images.githubusercontent.com/107942776/242320235-aa78978a-531d-4b94-a962-604f2de1ca25.png" width="600"/>

#### Project Serializers
<img src="https://user-images.githubusercontent.com/107942776/242320233-0fa479f6-28ee-43b8-bade-f78d0be4ce95.png" width="600"/>

## Tech Stacks
<div align="center">  
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>  
<a href="https://nextjs.org/" target="_blank" rel="noreferrer"> <img src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="nextjs" width="40" height="40"/>
</div>


## Contributors
- [Eric Frey](https://github.com/ericlfrey)
