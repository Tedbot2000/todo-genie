# ToDo Genie: A useful yet easy to user-friendly to-do list application

Do more with the Django application that is your daily manager for things you need to get done. 

## Key Features:

1. **User Authentication and Authorisation:** ToDo Genie uses AllAuth for user authentication and authorization, providing a secure way for users to create accounts and log in to access their personalised to-do lists.

2. **CRUD Operations:** The application supports Create, Read, Update, and Delete (CRUD) operations, enabling users to add, view, edit, and delete tasks as needed.

3. **Intuitive User Interface:** ToDo Genie features a user-friendly interface that makes it easy to navigate and manage tasks, with a clean design and minimal clutter.

4. **Task Status Toggle:** Users can easily toggle the status of their tasks between Not Started, In Progress, and Completed, helping them track their progress and stay organised.

5. **Task Deletion:** Users can delete tasks that are no longer relevant or completed, keeping their task list up-to-date and clutter-free.

6. **Responsive Design:** The application is designed to be responsive, ensuring a seamless user experience across various devices and screen sizes.


Image showing app on different devices


UX/UI
The application features a clean and minimalistic design, with a focus on usability and accessibility.
The task list is displayed in a table format, with columns for task name, status, and actions.
The application uses a responsive design, ensuring that it is usable on various devices and screen sizes.
Testing
[Insert information about testing frameworks and tools used]
[Insert information about testing coverage and results]

## ToDo Templates

### Base Template (`base.html`)

The base template provides a foundation for the application's layout and design, including the navigation bar, footer, and main content area. It uses Bootstrap for styling and layout, and includes custom CSS for additional design elements.

#### Meta Content:

- **Character Encoding:** The character encoding standard used in the template is set to UTF-8 to support a wide range of characters and languages.
- **Bootstrap Framework:** This is a widely-used CSS framework for building responsive and mobile-first interfaces.
- **Custom CSS:** The custom CSS stylesheet ('static/css/style.css') is used to visualy expand and enhance beyond bootstrap.
- **Fonts:** The font families used in the template are the Google fonts Roboto and Konkhmer Sleokchher, providing a clean and modern typography.

#### Navigation Bar:

The navigation bar is a critical component of the base template, providing links to essential pages and features of the application. It includes:

- **Login and Register Links:** Links to the login and register pages, allowing users to access their accounts or create new ones.
- **Logout Link:** A link to logout of the application, available only when the user is logged in.
- **Username Display:** The navigation bar displays the username of the logged-in user, providing a personalised experience.

#### Main Content:

The main content area displays:

- **Alert Messages:** Alert messages are displayed to provide feedback to the user. These messages are shown near the top of the card, ensuring they are visible without the need for scrolling. They are automatically dismissed after five seconds.
- **Primary UI Content:** Primary content from other HTML files is served below this.

#### Script References:

The base template includes references to the following scripts:

- **Bootstrap JavaScript Files:** The template includes references to Bootstrap's JavaScript files, which provide functionality for components such as dropdowns, modals, and tooltips.
- **Custom JavaScript Code:** The template also includes custom JavaScript code, which provides functionality for task management features, such as toggling task statuses and updating the task list.


### Main Page Template (todo_list.html)

The todo_list.html template serves as the main page of the application, displaying the user's task list and providing features for task management.

#### Meta Content:

- Extends the `base.html` template to ensure a consistent layout and styling across the entire application.
- Utilizes `{% load static %}` to load static files.

#### Content:

The todo_list.html template displays the following content:

- **Task Form:** The template includes a form for adding new tasks, allowing users to create new tasks and add them to their task list.
- **Task List:** The template displays the user's task list, including task names, statuses, and actions (delete).
- **Task Status Toggle:** The template provides a button for toggling task statuses, allowing users to easily update the status of their tasks.
    - If a task is not started the button will appear grey
    - If a task is in progress the button will appear orange
    - When a task is completed the button will appear green
- **Task Actions:** The template includes an action for deleting tasks, allowing users to remove tasks.


## ToDo Model

The toDo model is used to represent the tasks within the ToDo Genie Pro Django application. Below is an outline of the model's primary attributes and features:

### Fields:

The ToDo model includes the following fields to store and manage tasks, while associating them with a user:

- **id:** A unique identifier for each task, automatically generated by Django as a primary key.
- **todo_name:** A character field to store the title or name of the task, with a maximum length of 255 characters.
- **status:** A choice field to store the status of the task, with options including "not started", "in progress", and "completed".
- **user:** A foreign key field to store the user who created the task, linking the task to the User model.

##ToDo Views

The ToDo Views are responsible for handling the logic for each task-related action in the application. These views are defined in the **views.py** file and are called when a user interacts with the application.

Here are the Task Views defined in the **views.py** file:

**1. todo_list**

    - This view retrieves a list of all todo items from the database and renders the todo_list.html template, passing the list of todo items as a context variable.
    - The todo_list view is called when the user visits the root URL of the application ('').

**2. toggle_status**

    - This view takes an id parameter, which identifies the todo item to be updated.
    - The view toggles the completed status of the todo item and saves the changes to the database.
    - The toggle_status view is called when the user clicks the "Toggle Status" button for a todo item.

**3. delete_task**

    - This view takes an id parameter, which identifies the todo item to be deleted.
    - The view deletes the todo item from the database.
    - The delete_task view is called when the user clicks the "Delete" button for a todo item.

**4. update_task**

    - This view takes an id parameter, which identifies the todo item to be updated.
    - The view retrieves the todo item from the database, updates its details, and saves the changes to the database.
    - The update_task view is called when the user submits the "Update" form for a todo item.


**URL Routing**

The URL Routing system in Django maps URLs to views, which handle the logic for each page or action in the application. In the ToDo Genie application, the URL patterns are defined in the **urls.py** file.

In the ToDo Genie application, the **urls.py** file defines four URL patterns:

**Todo List Page:**
    -URL: '/'
    -View: 'todo_list'
    -Name: 'todo_list'
    -Function: Displays the list of tasks

**Toggle Task Status:**
    -URL: '/toggle_status/<int:id>/'
    -View: 'toggle_status'
    -Name: 'toggle_status'
    -Function: Toggles the status of a task

**Delete Task:**
    -URL: '/delete/<int:id>/'
    -View: 'delete_task'
    -Name: 'delete'
    -Function: Deletes a task

**Update Task:**
    -URL: '/update/<int:id>/'
    -View: 'update_task'
    -Name: 'update'
    -Function: Updates a task

By using URL Routing, the ToDo Genie application can decouple the URL structure from the view logic, making it easier to maintain and extend the application.



Deployment
The application is deployed on [insert deployment platform or service, e.g. Heroku, AWS].
[Insert information about deployment process and configuration]

Citation of ALL sources
[Insert citations for any code, images, or text used from external sources]
AllAuth: [insert citation for AllAuth library]
Django: [insert citation for Django framework]
[Insert citations for any other libraries or resources used]

Future Features
[Insert information about planned future features, e.g. due dates, reminders, task prioritization]
[Insert information about potential integrations with other services or APIs]
Known Bugs
[Insert information about known bugs or issues, e.g. browser compatibility issues, edge cases]
Technical Requirements
Python 3.x
Django 3.x
AllAuth 0.x
[Insert information about other dependencies or requirements]

Development Team
[Insert information about the development team, e.g. names, roles, contact information]

License
[Insert information about the license under which the application is released]
Note that this is just a draft, and you should fill in the placeholders with the actual information about your project. Additionally, you may want to add or remove sections depending on your specific needs.
