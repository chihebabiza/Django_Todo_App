# Django Todo List

A basic Django web application with an admin panel, models, views, and templates.

## Features
- Django admin panel for managing data.
- Dynamic pages powered by templates.
- Debug mode configurable via settings.
- SQLite database (default) — can be swapped with PostgreSQL/MySQL.
- Ready for development and production.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for the admin panel**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   * App: `http://127.0.0.1:8000/`
   * Admin Panel: `http://127.0.0.1:8000/admin/`

## Debug Mode

* In `settings.py`, set:

  ```python
  DEBUG = True  # Development (detailed error pages)
  DEBUG = False # Production (security + generic error pages)
  ```

## Project Structure

```
project-name/
│
├── manage.py
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_name/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── admin.py
└── requirements.txt
```


