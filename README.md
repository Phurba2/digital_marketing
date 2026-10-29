# Digital Marketing Course Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
</p>

A modern Django-based learning platform designed to help beginners explore digital marketing and SEO through structured courses, guided lessons, and progress tracking.

## Overview

This repository contains a lightweight course portal where users can:

- browse digital marketing and SEO learning paths
- view lesson details with embedded video content
- track progress as lessons are completed
- access a user dashboard tailored to their learning journey
- register and log in to maintain personal progress

The project is intentionally simple and beginner-friendly, making it a strong starting point for educational web applications built with Django.

## Key Features

- Course catalog for digital marketing and SEO topics
- Lesson-based learning flow with structured content
- Embedded YouTube video support
- User progress tracking for completed lessons
- Personalized dashboard experience
- SQLite-backed setup for local development
- Clean, template-driven frontend

## Tech Stack

- Python
- Django
- SQLite
- HTML / XHTML templates
- GitHub-ready project structure

## Project Structure

```text
digital_marketing/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── management/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.xhtml
│   ├── courses/
│   └── registration/
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── static/
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- virtual environment tool (optional but recommended)

### 1. Clone the repository

```bash
git clone https://github.com/Phurba2/digital_marketing.git
cd digital_marketing
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Then open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Application Behavior

The app includes the following flows:

- landing page for introducing the learning platform
- authenticated dashboard for user activity
- course detail pages
- lesson-specific video pages
- progress toggling for completed learning modules
- registration endpoint for new users

## Admin Access

To create an admin user:

```bash
python manage.py createsuperuser
```

Then sign in at:

```text
http://127.0.0.1:8000/admin/
```

## Configuration Notes

The project uses Django's default configuration with a custom `courses` app. Core configuration such as installed apps, URL routing, templates, static files, and login redirects are handled in `config/settings.py`.

## Roadmap

Potential future improvements include:

- richer course management through the admin panel
- quizzes and assessments
- different user roles and permissions
- search and filtering for courses
- progress analytics and completion reports
- authentication UX improvements

## Contributing

Contributions are welcome. If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project currently does not include a license file. If you plan to distribute or share it publicly, consider adding an appropriate open-source license such as MIT.

## Contact

For questions, feedback, or collaboration opportunities, please reach out via the GitHub repository owner profile.

---

Built for learners beginning their journey in digital marketing and SEO.
