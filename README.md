# Simple Event Planner - Django

A basic Event Planner web application made with Python and Django.

## Features
- Add an event
- View all events
- Edit an event
- Delete an event
- Store event information in SQLite database
- Simple clean interface
- Sample events included

## Technologies
- Python
- Django
- SQLite
- HTML
- CSS

## How to Run

1. Open a terminal in this folder.
2. Install Django:

```bash
pip install -r requirements.txt
```

3. Create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Add sample data:

```bash
python manage.py seed_data
```

5. Start the server:

```bash
python manage.py runserver
```

6. Open:

http://127.0.0.1:8000/

## Project Structure

```text
event_planner/
├── manage.py
├── requirements.txt
├── README.md
├── eventplanner/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── events/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    ├── management/
    │   └── commands/
    │       └── seed_data.py
    └── templates/
        └── events/
            ├── base.html
            ├── event_list.html
            └── event_form.html
```

## Main Django Concepts Used

- **Model:** Event data is stored using the Event model.
- **View:** Views handle adding, displaying, editing and deleting events.
- **Template:** HTML templates display the application pages.
- **URL routing:** URLs connect browser requests to views.
- **ORM:** Django ORM is used to save and retrieve events from SQLite.

## Viva Explanation

The application follows Django's MVT structure. The user opens a URL, Django sends the request to the correct view, the view communicates with the Event model/database, and then the result is displayed using an HTML template.

This is a simplified implementation created for learning and demonstration purposes.
