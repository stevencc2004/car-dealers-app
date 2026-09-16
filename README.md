# xrwvm-fullstack_developer_capstone

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
- **Deployment**: Render.com

## Features

- User authentication (login/logout/register)
- Dealer listing and filtering by state
- Dealer reviews with sentiment analysis
- Car brands and models management
- Responsive design with Bootstrap
- RESTful API endpoints

## API Endpoints

- `POST /djangoapp/login` - User login
- `GET /djangoapp/logout` - User logout
- `POST /djangoapp/register` - User registration
- `GET /fetchDealers` - Get all dealers
- `GET /fetchDealer/<id>` - Get dealer by ID
- `GET /fetchDealers/<state>` - Get dealers by state
- `GET /fetchReviews/dealer/<dealer_id>` - Get dealer reviews
- `POST /addReview` - Add a review
- `GET /getCarMakes` - Get car brands
- `GET /getCarModels` - Get car models
- `GET /analyze/<text>` - Analyze review sentiment

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
   git clone https://github.com/stevencc2004/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone
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
curl -X POST http://localhost:8000/djangoapp/login -H "Content-Type: application/json" -d '{"userName":"admin","password":"admin123"}'
```

### Logout
```bash
curl -X GET http://localhost:8000/djangoapp/logout
```

### Get All Dealers
```bash
curl http://localhost:8000/fetchDealers
```

### Get Dealer by ID
```bash
curl http://localhost:8000/fetchDealer/<dealer_id>
```

### Get Dealers by State (Kansas)
```bash
curl http://localhost:8000/fetchDealers/Kansas
```

### Get Dealer Reviews
```bash
curl http://localhost:8000/fetchReviews/dealer/<dealer_id>
```

### Analyze Review Sentiment
```bash
curl http://localhost:8000/analyze/Fantastic%20services
```

### Get Car Brands
```bash
curl http://localhost:8000/getCarMakes
```

### Get Car Models
```bash
curl http://localhost:8000/getCarModels
```

## Deployment

The application is deployed at: https://car-dealers-app-8000.proxy.cognitiveclass.ai

## CI/CD

GitHub Actions workflow automatically:
- Lints Python Files
- Lints JavaScript Files
- Deploys to production on push to main branch

## License

This project is licensed under the MIT License.