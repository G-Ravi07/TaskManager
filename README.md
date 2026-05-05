# Team Task Manager (Full-Stack)

A full-stack web application where teams can create projects, assign tasks, and track progress with role-based access control.

---

## Features

* Authentication (Signup/Login)
* Role-based access (Admin / Member)
* Project management
* Task creation and assignment
* Task status tracking (Pending, In Progress, Done)
* Dashboard with total and overdue tasks
* REST APIs using Django REST Framework
* Deployment ready with Railway

---

## Tech Stack

* Backend: Django, Django REST Framework
* Frontend: Django Templates (HTML, CSS)
* Database: SQLite (development), PostgreSQL (production)
* Deployment: Railway
* Server: Gunicorn

---

## Project Structure

```id="7k6r9n"
TaskManager/
│
├── config/
├── users/
├── projects/
├── tasks/
├── templates/
├── manage.py
├── requirements.txt
├── Procfile
```

---

## Setup Instructions

### Clone the repository

```id="s9d7pv"
git clone https://github.com/yourusername/taskmanager.git
cd taskmanager
```

---

### Create virtual environment

```id="zv1twd"
python -m venv venv
venv\Scripts\activate
```

---

### Install dependencies

```id="o4zx4s"
pip install -r requirements.txt
```

---

### Run migrations

```id="6y7i9f"
python manage.py migrate
```

---

### Run server

```id="y74u6b"
python manage.py runserver
```

---

## API Endpoints

* /api/projects/ (GET, POST)
* /api/tasks/ (GET, POST)

---

## Roles

Admin:

* Create projects
* Assign tasks

Member:

* View assigned tasks
* Update task status

---

## Dashboard

* Total tasks
* Overdue tasks
* User-specific task tracking

---

## Live Demo

(Add your Railway URL here after deployment)

---

## Demo Video

(Add your video link here)

---

## Author

Ravi G

git add .
git commit -m "added readme"
git push