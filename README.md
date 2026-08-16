# CRUD_App_NeuroFive-
CRUD App NeuroFive Solutions


# Event Scheduler & Manager

A Django-based **Event Scheduler and Manager CRUD application** for creating, viewing, updating, and deleting events. The application provides a clean Bootstrap 5.3 interface and uses PostgreSQL as the database.

## 🚀 Features

* Create and schedule events
* View all scheduled events
* Update existing events
* Delete events
* Search events
* Filter events by category
* Event status management
* Manager-based user roles
* Django authentication and authorization
* PostgreSQL database integration
* Responsive UI using Bootstrap 5.3
* Django Admin customization
* Success and error notifications

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5.3
* JavaScript
* tailwind CSS

### Backend

* Python
* Django
* Django ORM

### Database

* PostgreSQL

## 📁 Project Structure

```text
event_scheduler/es
│
├── manage.py
│
├── esapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/
│   ├── migrations/
│   ├── templates/
│   │   └── events/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
└── README.md
```

## ⚙️ Installation

Clone the project and enter the project directory:

```bash
git clone <repository-url>
cd event_scheduler
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🗄️ PostgreSQL Database Configuration

Create a PostgreSQL database:

```sql
CREATE DATABASE event_scheduler;
```

Create a PostgreSQL user:

```sql
CREATE USER event_scheduler_user WITH PASSWORD 'your_password';
```

Grant privileges:

```sql
GRANT ALL PRIVILEGES ON DATABASE event_scheduler TO event_scheduler_user;
```

Configure the database in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "event_scheduler",
        "USER": "event_scheduler_user",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

For production, database credentials should be stored in environment variables rather than directly in `settings.py`.

Example:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
```

## 🔄 Database Migrations

Run migrations after configuring PostgreSQL:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a Django superuser:

```bash
python manage.py createsuperuser
```

## 👤 User Roles

The application supports role-based access for users, particularly **Managers**.

### Manager

Managers can:

* Create events
* Schedule events
* View events
* Update events
* Delete events
* Search events
* Filter events
* Manage event information

### Superuser / Admin

Administrators can:

* Access Django Admin
* Manage users
* Manage managers
* Manage events
* Configure application data
* Perform administrative operations

Additional roles and permissions can be added using Django's built-in Groups and Permissions system.

## 📅 Event Management

The CRUD workflow allows managers to manage the complete event lifecycle.

### Create

Managers can create an event with information such as:

* Event title
* Date
* Description
* Status
* Category

### Read

Managers can view scheduled events from the event management interface.

### Update

Existing events can be edited when event information changes.

### Delete

Managers can delete events that are no longer required.

## 🔎 Search & Filtering

The event management page supports server-side searching and filtering.

Example:

```text
/manage/?search=conference&statusFilter=CONFERENCE
```

The `search` parameter searches event information, while `statusFilter` filters events based on the selected category.

## 🧩 Event Categories

The application supports categories such as:

```text
MEETING
WORKSHOP
CONFERENCE
SOCIAL
OTHER
```

These categories can be extended according to project requirements.

## 🔐 Authentication & Authorization

Django authentication is used to control access to protected functionality.

Recommended configuration includes:

* Login/logout functionality
* Authenticated manager access
* Django Groups
* Django Permissions
* Protected CRUD views
* Superuser administration

Example:

```python
from django.contrib.auth.decorators import login_required


@login_required
def manage_events(request):
    ...
```

For manager-specific access, Django Groups or custom permissions can be used.

## 🔔 Notifications

Django's messages framework is used to provide success and error notifications.

Example:

```python
from django.contrib import messages

messages.success(request, "Event created successfully!")
```

Error example:

```python
messages.error(request, "Unable to update event.")
```

## 🎨 Frontend

The application uses **Bootstrap 5.3** for responsive layouts and UI components.

Example Bootstrap CDN:

```html
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    rel="stylesheet"
>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

Custom CSS can be placed under:

```text
static/css/
```

## 🖥️ Run the Development Server

Start Django's development server:

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## 🔧 Environment Variables

For production, use a `.env` file or deployment environment variables.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=event_scheduler
DB_USER=event_scheduler_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Do not commit sensitive credentials or `.env` files to version control.

## 📦 Recommended Requirements

Example `requirements.txt`:

```text
Django
psycopg
```

Install them with:

```bash
pip install -r requirements.txt
```

## 🧪 Testing

Run Django's test suite:

```bash
python manage.py test
```

## 🔒 Production Considerations

Before deploying to production:

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use environment variables for secrets
* Use PostgreSQL
* Configure static files
* Configure HTTPS
* Set secure cookies
* Configure CSRF protection
* Use a production WSGI/ASGI server
* Configure proper database backups

## 📌 CRUD Workflow

```text
Manager Login
     │
     ▼
Event Management
     │
     ├── Create Event
     │
     ├── View Events
     │
     ├── Search / Filter
     │
     ├── Update Event
     │
     └── Delete Event
     │
     └── Add users, Allow access
     │
     └── Register/login

```

## 📄 License

This project is intended for educational and application-development purposes. Add the appropriate license here if the project is distributed publicly.

