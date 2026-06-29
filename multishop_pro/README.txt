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
# Note: If tables already exist in the database, register existing migrations using:
# python manage.py migrate multishop_userapp 0002 --fake

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

## Recent Changes

### Payment Processing & Receipts
- **Fixed `payment_view` NameError**: Corrected the undefined variable `razorpay_order_id` to `order_id` in the POST checkout block, allowing order and order item records to be created successfully.
- **Improved Success Redirection**: Redirected users to the `payment_success` receipt page upon successful transaction instead of straight to the order history.
- **Enhanced `payment_success_view`**: Added support for an optional `order_id` parameter to view/print the receipt of any specific past order. Implemented a fallback to fetch the latest order from the database if the session token is cleared or absent.

### Order History & Templates
- **Fixed "View Items" Collapse**: Changed the template attributes on the "View Items" button from Bootstrap 5 (`data-bs-toggle`/`data-bs-target`) to Bootstrap 4 (`data-toggle`/`data-target`) to restore the expand/collapse behavior.
- **Added "View Receipt" Links**: Integrated a "View Receipt" button next to each order in the history list, connecting directly to the printable payment receipt view.

## License

This project is licensed under the MIT License.
