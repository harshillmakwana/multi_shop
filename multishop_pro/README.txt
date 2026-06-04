# MultiShop Project

## Overview

The **MultiShop** project is a Django-based e‑commerce platform that supports multiple vendors, product catalogs, shopping carts, and order management. It includes a user-facing application (**multishop_userapp**) with views, templates, and an admin interface.

## Features

- Multi‑vendor support
- Product catalog and search
- Shopping cart and checkout flow
- User authentication and profile management
- Order history and address management
- Responsive HTML templates using Bootstrap

## Prerequisites

- Python 3.10+ (recommended 3.11)
- Django 5.0 or later
- PostgreSQL (or any Django‑compatible database)
- Virtual environment (`venv` or `conda`)

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd multishop_pro

# Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure the database in `multishop_pro/settings.py`
# Apply migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser
```

## Running the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to explore the application.

## Testing

```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes with clear messages.
4. Open a Pull Request.

## License

This project is licensed under the MIT License.
