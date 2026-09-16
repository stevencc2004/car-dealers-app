from django.core.management.base import BaseCommand
from dealers.mongo import get_dealers_collection, get_reviews_collection, get_cars_collection


class Command(BaseCommand):
    help = 'Seed the MongoDB database with sample data'

    def handle(self, *args, **kwargs):
        dealers = [
            {"name": "Kansas City Auto Mall", "city": "Kansas City", "state": "Kansas", "address": "1234 Main Street", "zip_code": "66101", "phone": "(913) 555-0101", "description": "Family-owned dealership serving Kansas City for over 20 years.", "image_url": ""},
            {"name": "Wichita Wheels", "city": "Wichita", "state": "Kansas", "address": "5678 Broadway Ave", "zip_code": "67201", "phone": "(316) 555-0202", "description": "Best prices on new and used cars in Wichita.", "image_url": ""},
            {"name": "Sunset Auto Sales", "city": "Los Angeles", "state": "California", "address": "901 Sunset Blvd", "zip_code": "90028", "phone": "(323) 555-0303", "description": "Premium car dealership in the heart of LA.", "image_url": ""},
            {"name": "Golden State Motors", "city": "San Francisco", "state": "California", "address": "456 Market Street", "zip_code": "94105", "phone": "(415) 555-0404", "description": "San Francisco's trusted car dealer since 1990.", "image_url": ""},
            {"name": "Manhattan Auto Gallery", "city": "New York", "state": "New York", "address": "789 Fifth Avenue", "zip_code": "10022", "phone": "(212) 555-0505", "description": "Luxury vehicles in the heart of Manhattan.", "image_url": ""},
            {"name": "Lone Star Dealership", "city": "Houston", "state": "Texas", "address": "321 Texas Ave", "zip_code": "77002", "phone": "(713) 555-0606", "description": "Everything's bigger in Texas, including our inventory.", "image_url": ""},
            {"name": "Sunshine State Cars", "city": "Miami", "state": "Florida", "address": "654 Ocean Drive", "zip_code": "33139", "phone": "(305) 555-0707", "description": "Drive in style with our premium Florida collection.", "image_url": ""},
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
            {"brand": "Nissan", "model": "Altima", "year": 2024, "price": 26000},
        ]

        dc = get_dealers_collection()
        if dc.count_documents({}) == 0:
            result = dc.insert_many(dealers)
            self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} dealers'))
            for i, dealer_id in enumerate(result.inserted_ids[:3]):
                get_reviews_collection().insert_one({
                    "dealer_id": str(dealer_id),
                    "name": ["John D.", "Sarah M.", "Mike R."][i],
                    "review": ["Great experience!", "Fantastic services!", "Average experience."][i],
                    "sentiment": ["positive", "positive", "neutral"][i],
                    "user": ["john_doe", "sarah_m", "mike_r"][i],
                })
            self.stdout.write(self.style.SUCCESS('Inserted 3 reviews'))
        else:
            self.stdout.write(self.style.WARNING('Dealers already exist, skipping'))

        cc = get_cars_collection()
        if cc.count_documents({}) == 0:
            result = cc.insert_many(car_models)
            self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} car models'))
        else:
            self.stdout.write(self.style.WARNING('Cars already exist, skipping'))