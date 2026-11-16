# Task Management System

## Project Overview

The **Task Management System** is a web-based application developed using Python and Django. It helps users manage their daily tasks efficiently by allowing them to create, view, update, and delete tasks.

The application provides user authentication so that each user can manage their own tasks securely.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Features

- **User Registration:** New users can create an account.
- **User Login:** Registered users can securely log in.
- **Add Tasks:** Users can create new tasks.
- **View Tasks:** Users can view their assigned tasks.
- **Update Tasks:** Users can modify existing tasks.
- **Delete Tasks:** Users can remove tasks.
- **Task Status Management:** Users can manage task statuses such as Pending and Completed.
- **User-Specific Tasks:** Each user can access and manage their own tasks.
- **Logout:** Users can securely log out of the application.

## Project Structure

```text
Authentication/
│
├── authen/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Authentication/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks_manage/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
├── templates/
├── .gitignore
├── requirements.txt
├── db.sqlite3
├── manage.py
└── README.md
```

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/insanedingo23/Task-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Task-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Django Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Database

The application uses SQLite as its database.

Django models are used to manage application data, including user-related task information.

## Future Enhancements

- Task deadlines and reminders.
- Task priority management.
- Search and filtering functionality.
- Dashboard with task statistics.
- Improved user interface and responsive design.
- Uploading files such as images and documents.

## Author

**Developed as a Python Django project.**

## Project Status

Currently under development. More features and improvements will be added in future updates.