# Tisha Patience Malongo — Portfolio

A bold, dark-themed developer portfolio built with **Python**, **Django**, **Tailwind CSS**, **HTML**, and **CSS**.

## Features

- Typing hero animation
- Scroll-reveal animations
- Animated skill bars
- Dynamic project cards (managed via Django admin)
- Contact form (saves to DB + optional email)
- Django admin panel to manage all content

---

## Quick Start

### 1. Clone / download the project

```bash
cd portfolio
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Load sample data (optional)

```bash
python manage.py shell < seed_data.py
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to see your portfolio.
Visit **http://127.0.0.1:8000/admin** to manage projects, skills, and messages.

---

## Customisation

### Change your name & bio
Edit `templates/core/home.html` — search for "Alex Dev" and update to your name, email, GitHub/LinkedIn URLs, and bio paragraph.

### Add projects
Go to `/admin` → Projects → Add Project.
- Set **Featured = True** for the top 3 (shown as cards)
- Other projects appear as a compact list below

### Add skills
Go to `/admin` → Skills → Add Skill.
Categories: `languages`, `frameworks`, `tools`, `databases`

### Change accent colour
Open `templates/core/home.html`, find `tailwind.config` and change `'brand': '#FF5C00'` to any hex you like.

### Add a real CV
Drop your CV as `static/cv.pdf` — the "Download CV" button links to it automatically.

### Enable email sending
In `config/settings.py`, replace:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
with your SMTP settings (e.g. Gmail, SendGrid). Also update `your@email.com` in `core/views.py`.

---

## Project Structure

```
portfolio/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── models.py        # Project, Skill, ContactMessage
│   ├── views.py         # Single home view
│   ├── forms.py         # ContactForm
│   ├── admin.py         # Admin config
│   └── urls.py
├── templates/
│   └── core/
│       └── home.html    # Main template
├── static/
│   ├── css/style.css    # Custom styles
│   └── js/main.js       # Animations & interactions
├── seed_data.py          # Sample data loader
├── manage.py
└── requirements.txt
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Django 4.2 |
| Frontend | HTML5, Tailwind CSS (CDN), Vanilla JS |
| Database | SQLite (dev) / PostgreSQL (production) |
| Styling | CSS custom properties, JetBrains Mono font |
