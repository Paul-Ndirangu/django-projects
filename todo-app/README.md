## Django To-Do App

This is a simple to-do application built using the Django web framework. It allows users to:

* **Create and manage tasks**: Add new tasks, mark them as completed, and edit existing ones.
* **Organize tasks**: Filter tasks by completed status, due date, and priority.
* **Admin panel**: Users with admin privileges can access and manage all tasks in the system.

### Features

* User authentication and authorization
* CRUD operations for tasks
* Task filtering and sorting
* Admin panel for user management and task overview
* Optional due dates and priorities for tasks

### Prerequisites

* Python 3.6+
* Django framework
* A database 

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Paul-Ndirangu/django-projects
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your database settings in `settings.py`.

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser for the admin panel:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Access the app at http://127.0.0.1:8000/

### Contributing

We welcome contributions to this project! Please see the CONTRIBUTING.md file for guidelines.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

