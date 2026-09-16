from pymongo import MongoClient
import json

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'car_dealers'

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

dealers = [
    {
        "name": "Kansas City Auto Mall",
        "city": "Kansas City",
        "state": "Kansas",
        "address": "1234 Main Street",
        "zip_code": "66101",
        "phone": "(913) 555-0101",
        "description": "Family-owned dealership serving Kansas City for over 20 years.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Wichita Wheels",
        "city": "Wichita",
        "state": "Kansas",
        "address": "5678 Broadway Ave",
        "zip_code": "67201",
        "phone": "(316) 555-0202",
        "description": "Best prices on new and used cars in Wichita.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Sunset Auto Sales",
        "city": "Los Angeles",
        "state": "California",
        "address": "901 Sunset Blvd",
        "zip_code": "90028",
        "phone": "(323) 555-0303",
        "description": "Premium car dealership in the heart of LA.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Golden State Motors",
        "city": "San Francisco",
        "state": "California",
        "address": "456 Market Street",
        "zip_code": "94105",
        "phone": "(415) 555-0404",
        "description": "San Francisco's trusted car dealer since 1990.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Manhattan Auto Gallery",
        "city": "New York",
        "state": "New York",
        "address": "789 Fifth Avenue",
        "zip_code": "10022",
        "phone": "(212) 555-0505",
        "description": "Luxury vehicles in the heart of Manhattan.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Lone Star Dealership",
        "city": "Houston",
        "state": "Texas",
        "address": "321 Texas Ave",
        "zip_code": "77002",
        "phone": "(713) 555-0606",
        "description": "Everything's bigger in Texas, including our inventory.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    },
    {
        "name": "Sunshine State Cars",
        "city": "Miami",
        "state": "Florida",
        "address": "654 Ocean Drive",
        "zip_code": "33139",
        "phone": "(305) 555-0707",
        "description": "Drive in style with our premium Florida collection.",
        "image_url": "https://images.unsplash.com/photo-1562141961-54091e47f58c?w=400"
    }
]

reviews = [
    {
        "dealer_id": None,
        "name": "John D.",
        "review": "Great experience! The staff was very helpful and professional.",
        "sentiment": "positive",
        "user": "john_doe"
    },
    {
        "dealer_id": None,
        "name": "Sarah M.",
        "review": "Fantastic services and great prices. Highly recommended!",
        "sentiment": "positive",
        "user": "sarah_m"
    },
    {
        "dealer_id": None,
        "name": "Mike R.",
        "review": "Average experience. Could improve customer service.",
        "sentiment": "neutral",
        "user": "mike_r"
    },
    {
        "dealer_id": None,
        "name": "Lisa K.",
        "review": "Good selection of cars but the wait time was too long.",
        "sentiment": "neutral",
        "user": "lisa_k"
    },
    {
        "dealer_id": None,
        "name": "James W.",
        "review": "Excellent customer service and great prices!",
        "sentiment": "positive",
        "user": "james_w"
    },
    {
        "dealer_id": None,
        "name": "Maria G.",
        "review": "Very satisfied with my purchase. Highly recommended!",
        "sentiment": "positive",
        "user": "maria_g"
    },
    {
        "dealer_id": None,
        "name": "Robert T.",
        "review": "Terrible experience. Will not come back again.",
        "sentiment": "negative",
        "user": "robert_t"
    }
]

car_brands = [
    {"name": "Toyota"},
    {"name": "Honda"},
    {"name": "Ford"},
    {"name": "Chevrolet"},
    {"name": "BMW"},
    {"name": "Mercedes-Benz"},
    {"name": "Audi"},
    {"name": "Nissan"},
    {"name": "Hyundai"},
    {"name": "Kia"}
]

car_models = [
    {"brand": "Toyota", "model": "Camry", "year": 2024, "price": 28000},
    {"brand": "Toyota", "model": "Corolla", "year": 2024, "price": 22000},
    {"brand": "Honda", "model": "Civic", "year": 2024, "price": 24000},
    {"brand": "Honda", "model": "Accord", "year": 2024, "price": 27000},
    {"brand": "Ford", "model": "Mustang", "year": 2024, "price": 35000},
    {"brand": "Ford", "model": "F-150", "year": 2024, "price": 42000},
    {"brand": "Chevrolet", "model": "Silverado", "year": 2024, "price": 40000},
    {"brand": "BMW", "model": "3 Series", "year": 2024, "price": 45000},
    {"brand": "Mercedes-Benz", "model": "C-Class", "year": 2024, "price": 48000},
    {"brand": "Nissan", "model": "Altima", "year": 2024, "price": 26000}
]

print("Seeding database...")

db.dealers.drop()
result = db.dealers.insert_many(dealers)
print(f"Inserted {len(result.inserted_ids)} dealers")

for i, dealer_id in enumerate(result.inserted_ids):
    reviews[i]["dealer_id"] = str(dealer_id)

db.reviews.drop()
result = db.reviews.insert_many(reviews)
print(f"Inserted {len(result.inserted_ids)} reviews")

db.cars.drop()
result = db.cars.insert_many(car_models)
print(f"Inserted {len(result.inserted_ids)} car models")

print("Database seeded successfully!")