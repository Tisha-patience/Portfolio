"""
Run this after migrations to populate sample data:
    python manage.py shell < seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Project, Skill

# Clear existing
Project.objects.all().delete()
Skill.objects.all().delete()

# Sample projects
projects = [
    {
        'title': 'Task Flow API',
        'description': 'A RESTful task management API built with Django REST Framework. Features JWT authentication, team workspaces, and real-time progress tracking. Deployed on Railway with PostgreSQL.',
        'tech_stack': 'Python, Django, DRF, PostgreSQL, JWT',
        'github_url': 'https://github.com/yourusername/task-flow-api',
        'live_url': 'https://taskflow.example.com',
        'featured': True,
        'order': 1,
    },
    {
        'title': 'Weather Dashboard',
        'description': 'A responsive weather app that fetches real-time data from OpenWeather API. Built with vanilla JS and styled with Tailwind CSS, served via a lightweight Django backend.',
        'tech_stack': 'Python, Django, JavaScript, Tailwind CSS, REST API',
        'github_url': 'https://github.com/yourusername/weather-dashboard',
        'live_url': 'https://weather.example.com',
        'featured': True,
        'order': 2,
    },
    {
        'title': 'Dev Blog Engine',
        'description': 'A Markdown-powered blog engine with syntax highlighting, tag filtering, and an RSS feed. Built to learn Django\'s ORM and template system from the ground up.',
        'tech_stack': 'Python, Django, SQLite, Markdown, CSS',
        'github_url': 'https://github.com/yourusername/dev-blog',
        'live_url': '',
        'featured': True,
        'order': 3,
    },
    {
        'title': 'CLI Budget Tracker',
        'description': 'A command-line personal finance tracker with CSV import/export, monthly summaries, and category-based spending reports using Python\'s standard library.',
        'tech_stack': 'Python, CSV, argparse',
        'github_url': 'https://github.com/yourusername/budget-tracker',
        'live_url': '',
        'featured': False,
        'order': 4,
    },
]

for p in projects:
    Project.objects.create(**p)
    print(f"Created project: {p['title']}")

# Sample skills
skills = [
    # Languages
    {'name': 'Python', 'category': 'languages', 'proficiency': 80, 'order': 1},
    {'name': 'JavaScript', 'category': 'languages', 'proficiency': 65, 'order': 2},
    {'name': 'HTML', 'category': 'languages', 'proficiency': 90, 'order': 3},
    {'name': 'CSS', 'category': 'languages', 'proficiency': 85, 'order': 4},
    {'name': 'SQL', 'category': 'languages', 'proficiency': 60, 'order': 5},
    # Frameworks
    {'name': 'Django', 'category': 'frameworks', 'proficiency': 75, 'order': 1},
    {'name': 'Tailwind CSS', 'category': 'frameworks', 'proficiency': 80, 'order': 2},
    {'name': 'Django REST Framework', 'category': 'frameworks', 'proficiency': 65, 'order': 3},
    # Tools
    {'name': 'Git & GitHub', 'category': 'tools', 'proficiency': 75, 'order': 1},
    {'name': 'VS Code', 'category': 'tools', 'proficiency': 90, 'order': 2},
    {'name': 'Linux / CLI', 'category': 'tools', 'proficiency': 70, 'order': 3},
    {'name': 'Docker', 'category': 'tools', 'proficiency': 45, 'order': 4},
    # Databases
    {'name': 'SQLite', 'category': 'databases', 'proficiency': 75, 'order': 1},
    {'name': 'PostgreSQL', 'category': 'databases', 'proficiency': 55, 'order': 2},
]

for s in skills:
    Skill.objects.create(**s)
    print(f"Created skill: {s['name']}")

print("\nSeed data loaded successfully!")
