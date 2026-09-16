# Car Dealers App

A full-stack web application for finding and reviewing car dealerships, built with Django, React, and MongoDB.

## Project Overview

Car Dealers App allows users to:
- Browse car dealerships by state
- Read and submit dealer reviews
- Analyze review sentiment
- User authentication (login/register)
- Admin panel for managing dealers, reviews, and car brands/models

## Technology Stack

- **Backend**: Django 6.1, Django REST Framework
- **Frontend**: HTML/CSS, Bootstrap 5, React
- **Database**: MongoDB
- **CI/CD**: GitHub Actions
- **Deployment**: Cloud platform (IBM Cloud/AWS/Heroku)

## Features

- User authentication (login/logout/register)
- Dealer listing and filtering by state
- Dealer reviews with sentiment analysis
- Car brands and models management
- Responsive design with Bootstrap
- RESTful API endpoints

## API Endpoints

- `POST /api/login/` - User login
- `POST /api/logout/` - User logout
- `POST /api/register/` - User registration
- `GET /api/dealers/` - Get all dealers
- `GET /api/dealers/<id>/` - Get dealer by ID
- `GET /api/dealers/state/<state>/` - Get dealers by state
- `GET /api/reviews/<dealer_id>/` - Get dealer reviews
- `POST /api/reviews/` - Add a review
- `GET /api/cars/brands/` - Get car brands
- `GET /api/cars/models/` - Get car models
- `GET /api/analyze/?text=<text>` - Analyze review sentiment

## Project Structure

```
├── server/
│   ├── server_project/    # Django project settings
│   ├── dealers/           # Main Django app
│   ├── frontend/
│   │   ├── static/        # HTML templates
│   │   └── src/           # React components
│   └── manage.py
├── .github/
│   └── workflows/         # CI/CD configuration
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd car-dealers-app
   ```

2. Install Python dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers pymongo
   ```

3. Start MongoDB server

4. Run migrations:
   ```bash
   cd server
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Seed the database with sample data

7. Run the server:
   ```bash
   python manage.py runserver
   ```

## Testing cURL Commands

### Login
```bash
curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass123"}'
```

### Logout
```bash
curl -X POST http://localhost:8000/api/logout/
```

### Get All Dealers
```bash
curl http://localhost:8000/api/dealers/
```

### Get Dealer by ID
```bash
curl http://localhost:8000/api/dealers/<dealer_id>/
```

### Get Dealers by State (Kansas)
```bash
curl http://localhost:8000/api/dealers/state/Kansas/
```

### Get Dealer Reviews
```bash
curl http://localhost:8000/api/reviews/<dealer_id>/
```

### Analyze Review Sentiment
```bash
curl "http://localhost:8000/api/analyze/?text=fantastic+services"
```

### Get Car Brands
```bash
curl http://localhost:8000/api/cars/brands/
```

### Get Car Models
```bash
curl http://localhost:8000/api/cars/models/
```

## Deployment

The application is deployed at: [Deployment URL]

## CI/CD

GitHub Actions workflow automatically:
- Runs tests
- Lints code
- Deploys to production on push to main branch

## License

This project is licensed under the MIT License.