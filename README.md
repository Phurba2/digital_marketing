# Digital Marketing Course Platform

A Django-based learning platform for beginners exploring digital marketing and SEO. This project helps learners browse courses, watch lesson videos, track progress, and build practical knowledge through a simple, structured learning experience.

## Overview

This repository is designed as a compact educational app where users can:

- Browse digital marketing and SEO courses
- Open detailed lesson pages with embedded video content
- Track lesson completion progress
- View a personal dashboard of completed learning milestones
- Register and log in to manage their progress

The project blends a lightweight Django backend with template-driven HTML pages to create a beginner-friendly course portal.

## Features

- Course catalog with SEO and digital marketing learning tracks
- Lesson-by-lesson content structure
- Embedded YouTube video support
- Progress tracking with user completion records
- Dashboard for learners to review progress
- Clean, responsive template-based front end
- SQLite database for quick local setup

## Tech Stack

- Python
- Django
- SQLite
- HTML / XHTML templates
- Bootstrap-inspired UI styling

## Project Structure

```text
digital_marketing/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
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
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Phurba2/digital_marketing.git
cd digital_marketing
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/macOS
# .venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

## App Workflow

The platform includes:

- A landing page for introducing the learning experience
- A dashboard for signed-in users
- Detailed course pages
- Lesson detail pages with video playback
- A progress toggle mechanism to mark lessons as completed

## Default Django Setup

This project is built using Django's default project structure with a custom `courses` app. The application is configured in `config/settings.py` and route handling is defined in `courses/urls.py`.

## Future Enhancements

Potential ideas for growing this project include:

- Admin-created course management via a richer CMS experience
- User profiles and achievements
- Quizzes and certifications
- Search and filtering by topic
- Payment or premium content access

## License

This project does not currently include a license file. If you plan to distribute it publicly, consider adding an open-source license such as MIT.

## Contributing

Contributions are welcome. If you'd like to improve the platform, feel free to:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## Contact

For questions or collaboration inquiries, please reach out through the repository owner profile on GitHub.

---

Built for learners starting their journey in digital marketing and SEO.
