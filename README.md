# AgriPet Livestock & Pet Store System

A comprehensive Django web application for managing livestock and pet stores with inventory management, sales processing, attendance tracking, and more.
Agripet Inventory Management System
Developed by: DEVERLY GIO

Copyright © 2026 All Rights Reserved.
## Features

### 🔐 Authentication
- Email-based login system
- Secure user authentication using Django's built-in auth

### 📊 Dashboard
- Today's sales summary
- Total inventory stock
- Low stock alerts (< 5 units)
- Recent sales overview
- Interactive charts (weekly sales, category breakdown)

### 📦 Inventory Management
- Add, edit, delete products
- Product categories: Chicken, Pig, Dog, Cat, Feeds
- Multi-store support (Livestock Store, AgriPet Store)
- Stock level tracking with color-coded alerts
- Image upload for products
- Low stock monitoring

### 🛒 Sales System
- Store selection for purchases
- Shopping cart functionality
- Quantity management
- Automatic total calculation
- Payment proof upload (required)
- Order processing and confirmation
- Owner email tracking
- Automatic stock deduction

### 👥 Attendance System
- Staff time-in/time-out tracking
- Daily attendance records
- Staff management per store
- Role-based access

### 📧 Email Notifications
- New sale notifications to owners
- Order status change alerts
- Low stock alerts to administrators
- Configurable email settings

## Tech Stack

- **Backend**: Django 6.0.2 (Python)
- **Database**: SQLite (development) / MySQL (production)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript, Chart.js
- **Media Handling**: Django file uploads

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Clone/Download the Project
```bash
cd "C:\Users\User\OneDrive\Desktop\Livestock & AgriPet Store System"
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6. Populate Sample Data (Optional)
```bash
python manage.py populate_sample_data
```
This creates sample stores, products, customers, staff, and orders for testing.

### 7. Configure Email (Optional)
Update `config/settings.py` with your email settings:
```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### 8. Run the Server
```bash
python manage.py runserver
```
Access at: http://127.0.0.1:8000/

## Usage

### Login
- Use the admin credentials created during setup
- Default: username: admin, password: admin123

### Dashboard
- View key metrics and recent activity
- Access all main features from the navigation

### Inventory Management
- Navigate to "Inventory" to view all products
- Use filters to find specific items
- Add new products with images
- Edit or delete existing products

### Sales Processing
- Go to "Shop" to browse products
- Add items to cart
- Select quantities
- Upload payment proof during checkout
- Complete the sale

### Attendance Tracking
- Access "Attendance" section
- Record staff time-in/out
- View attendance history with filters

## Management Commands

### Populate Sample Data
```bash
python manage.py populate_sample_data
```
Creates sample data for testing and demonstration.

### Send Low Stock Alerts
```bash
python manage.py send_low_stock_alerts
```
Sends email alerts to administrators about low stock items. Can be run as a cron job.

## Email Notifications

The system sends automated email notifications for:

- **New Sales**: When orders are placed
- **Status Changes**: When order status is updated
- **Low Stock Alerts**: When products reach minimum stock levels

Configure email settings in `config/settings.py` or environment variables.

## Database Configuration

### Development (SQLite)
The project uses SQLite by default for development.

### Production (MySQL)
For production, update `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agripet_store',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Install MySQL connector:
```bash
pip install mysqlclient
```

## Project Structure

```
livestock_system/
├── config/                 # Django settings
├── store/                  # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── forms.py           # Form definitions
│   ├── admin.py           # Admin interface
│   ├── urls.py            # URL routing
│   ├── apps.py            # App config
│   ├── management/        # Custom management commands
│   │   └── commands/      # populate_sample_data, send_low_stock_alerts
│   └── templates/         # HTML templates
├── db.sqlite3             # Database file
├── manage.py              # Django management script
├── media/                 # Uploaded files
└── staticfiles/           # Static files
```

## Models Overview

- **Store**: Multiple store locations
- **Product**: Inventory items with categories
- **Customer**: Buyer information
- **Order**: Purchase transactions
- **OrderItem**: Individual items in orders
- **PaymentProof**: Uploaded payment receipts
- **Staff**: Store employees
- **Attendance**: Time tracking records

## Security Features

- CSRF protection on all forms
- User authentication required
- Secure file uploads
- SQL injection prevention
- XSS protection

## API Endpoints

The system provides JSON endpoints for charts:

- `/dashboard/weekly-sales-data/` - Weekly sales data
- `/dashboard/category-sales-data/` - Sales by category

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please contact the development team.
