from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017')
db = client['car_dealers']

# Clear existing data
db.dealers.delete_many({})
db.reviews.delete_many({})

# 50 Dealers
dealers = [
    {"name": "Kansas City Auto Mall", "city": "Kansas City", "state": "Kansas", "address": "1234 Main Street", "zip_code": "66101", "phone": "(913) 555-0101", "description": "Family-owned dealership serving Kansas City for over 20 years.", "lat": "39.0997", "long": "-94.5786"},
    {"name": "Wichita Wheels", "city": "Wichita", "state": "Kansas", "address": "5678 Broadway Ave", "zip_code": "67201", "phone": "(316) 555-0202", "description": "Best prices on new and used cars in Wichita.", "lat": "37.6872", "long": "-97.3301"},
    {"name": "Topeka Motors", "city": "Topeka", "state": "Kansas", "address": "910 Kansas Ave", "zip_code": "66603", "phone": "(785) 555-0303", "description": "Topeka's trusted dealer since 1985.", "lat": "39.0473", "long": "-95.6752"},
    {"name": "Lawrence Auto Sales", "city": "Lawrence", "state": "Kansas", "address": "234 Massachusetts St", "zip_code": "66044", "phone": "(785) 555-0404", "description": "Quality vehicles at affordable prices.", "lat": "38.9717", "long": "-95.2353"},
    {"name": "Sunset Auto Sales", "city": "Los Angeles", "state": "California", "address": "901 Sunset Blvd", "zip_code": "90028", "phone": "(323) 555-0505", "description": "Premium car dealership in the heart of LA.", "lat": "34.0522", "long": "-118.2437"},
    {"name": "Golden State Motors", "city": "San Francisco", "state": "California", "address": "456 Market Street", "zip_code": "94105", "phone": "(415) 555-0606", "description": "San Francisco's trusted car dealer since 1990.", "lat": "37.7749", "long": "-122.4194"},
    {"name": "San Diego Car Center", "city": "San Diego", "state": "California", "address": "789 Pacific Hwy", "zip_code": "92101", "phone": "(619) 555-0707", "description": "Best selection in San Diego.", "lat": "32.7157", "long": "-117.1611"},
    {"name": "Sacramento Auto World", "city": "Sacramento", "state": "California", "address": "321 J Street", "zip_code": "95814", "phone": "(916) 555-0808", "description": "Capital city's premier dealership.", "lat": "38.5816", "long": "-121.4944"},
    {"name": "Manhattan Auto Gallery", "city": "New York", "state": "New York", "address": "789 Fifth Avenue", "zip_code": "10022", "phone": "(212) 555-0909", "description": "Luxury vehicles in the heart of Manhattan.", "lat": "40.7128", "long": "-74.0060"},
    {"name": "Brooklyn Motors", "city": "Brooklyn", "state": "New York", "address": "456 Atlantic Ave", "zip_code": "11217", "phone": "(718) 555-1010", "description": "Brooklyn's best car deals.", "lat": "40.6782", "long": "-73.9442"},
    {"name": "Buffalo Auto Exchange", "city": "Buffalo", "state": "New York", "address": "123 Main Street", "zip_code": "14202", "phone": "(716) 555-1111", "description": "Western New York's top dealer.", "lat": "42.8864", "long": "-78.8784"},
    {"name": "Rochester Car Sales", "city": "Rochester", "state": "New York", "address": "321 East Ave", "zip_code": "14604", "phone": "(585) 555-1212", "description": "Quality used cars in Rochester.", "lat": "43.1566", "long": "-77.6088"},
    {"name": "Lone Star Dealership", "city": "Houston", "state": "Texas", "address": "321 Texas Ave", "zip_code": "77002", "phone": "(713) 555-1313", "description": "Everything's bigger in Texas, including our inventory.", "lat": "29.7604", "long": "-95.3698"},
    {"name": "Dallas Auto Ranch", "city": "Dallas", "state": "Texas", "address": "654 Commerce St", "zip_code": "75201", "phone": "(214) 555-1414", "description": "Dallas's premier car dealership.", "lat": "32.7767", "long": "-96.7970"},
    {"name": "San Antonio Motors", "city": "San Antonio", "state": "Texas", "address": "987 River Walk", "zip_code": "78205", "phone": "(210) 555-1515", "description": "Alamo City's trusted dealer.", "lat": "29.4241", "long": "-98.4936"},
    {"name": "Austin Car Company", "city": "Austin", "state": "Texas", "address": "111 Congress Ave", "zip_code": "78701", "phone": "(512) 555-1616", "description": "Keep Austin driving.", "lat": "30.2672", "long": "-97.7431"},
    {"name": "Sunshine State Cars", "city": "Miami", "state": "Florida", "address": "654 Ocean Drive", "zip_code": "33139", "phone": "(305) 555-1717", "description": "Drive in style with our premium Florida collection.", "lat": "25.7617", "long": "-80.1918"},
    {"name": "Orlando Auto World", "city": "Orlando", "state": "Florida", "address": "321 Orange Ave", "zip_code": "32801", "phone": "(407) 555-1818", "description": "Theme park of car deals.", "lat": "28.5383", "long": "-81.3792"},
    {"name": "Tampa Bay Motors", "city": "Tampa", "state": "Florida", "address": "456 Bayshore Blvd", "zip_code": "33606", "phone": "(813) 555-1919", "description": "Tampa's #1 car dealer.", "lat": "27.9506", "long": "-82.4572"},
    {"name": "Jacksonville Auto Sales", "city": "Jacksonville", "state": "Florida", "address": "789 Bay Street", "zip_code": "32202", "phone": "(904) 555-2020", "description": "Northeast Florida's best deals.", "lat": "30.3322", "long": "-81.6557"},
    {"name": "Chicago Car Palace", "city": "Chicago", "state": "Illinois", "address": "123 Michigan Ave", "zip_code": "60601", "phone": "(312) 555-2121", "description": "Windy City's top dealership.", "lat": "41.8781", "long": "-87.6298"},
    {"name": "Springfield Auto Mart", "city": "Springfield", "state": "Illinois", "address": "456 Capitol Ave", "zip_code": "62701", "phone": "(217) 555-2222", "description": "Illinois capital's trusted dealer.", "lat": "39.7817", "long": "-89.6501"},
    {"name": "Naperville Motors", "city": "Naperville", "state": "Illinois", "address": "789 Washington St", "zip_code": "60540", "phone": "(630) 555-2323", "description": "Suburban car excellence.", "lat": "41.7508", "long": "-88.1535"},
    {"name": "Rockford Auto Exchange", "city": "Rockford", "state": "Illinois", "address": "321 State Street", "zip_code": "61101", "phone": "(815) 555-2424", "description": "Rockford's best car deals.", "lat": "42.2711", "long": "-89.0940"},
    {"name": "Phoenix Rising Motors", "city": "Phoenix", "state": "Arizona", "address": "555 Camelback Rd", "zip_code": "85012", "phone": "(602) 555-2525", "description": "Desert deals on wheels.", "lat": "33.4484", "long": "-112.0740"},
    {"name": "Tucson Auto Center", "city": "Tucson", "state": "Arizona", "address": "888 Oracle Rd", "zip_code": "85705", "phone": "(520) 555-2626", "description": "Arizona's second city, first in car deals.", "lat": "32.2226", "long": "-110.9747"},
    {"name": "Denver Mountain Motors", "city": "Denver", "state": "Colorado", "address": "1600 Broadway", "zip_code": "80202", "phone": "(303) 555-2727", "description": "Mile high car deals.", "lat": "39.7392", "long": "-104.9903"},
    {"name": "Colorado Springs Auto", "city": "Colorado Springs", "state": "Colorado", "address": "222 Tejon St", "zip_code": "80903", "phone": "(719) 555-2828", "description": "Pikes Peak premier dealer.", "lat": "38.8339", "long": "-104.8214"},
    {"name": "Seattle Auto Hub", "city": "Seattle", "state": "Washington", "address": "400 Pine Street", "zip_code": "98101", "phone": "(206) 555-2929", "description": "Emerald City's car connection.", "lat": "47.6062", "long": "-122.3321"},
    {"name": "Tacoma Motors", "city": "Tacoma", "state": "Washington", "address": "700 Pacific Ave", "zip_code": "98402", "phone": "(253) 555-3030", "description": "City of Destiny's dealership.", "lat": "47.2529", "long": "-122.4443"},
    {"name": "Portland Auto Gallery", "city": "Portland", "state": "Oregon", "address": "501 SW Broadway", "zip_code": "97205", "phone": "(503) 555-3131", "description": "Rose City's car collection.", "lat": "45.5152", "long": "-122.6784"},
    {"name": "Salem Car Center", "city": "Salem", "state": "Oregon", "address": "200 Liberty St", "zip_code": "97301", "phone": "(503) 555-3232", "description": "Capital city car deals.", "lat": "44.9429", "long": "-123.0351"},
    {"name": "Atlanta Premier Motors", "city": "Atlanta", "state": "Georgia", "address": "333 Peachtree St", "zip_code": "30308", "phone": "(404) 555-3333", "description": "Peach state's top dealer.", "lat": "33.7490", "long": "-84.3880"},
    {"name": "Savannah Auto Sales", "city": "Savannah", "state": "Georgia", "address": "100 River Street", "zip_code": "31401", "phone": "(912) 555-3434", "description": "Historic city, modern deals.", "lat": "32.0809", "long": "-81.0912"},
    {"name": "Nashville Auto Exchange", "city": "Nashville", "state": "Tennessee", "address": "222 Broadway", "zip_code": "37201", "phone": "(615) 555-3535", "description": "Music City's car harmony.", "lat": "36.1627", "long": "-86.7816"},
    {"name": "Memphis Motors", "city": "Memphis", "state": "Tennessee", "address": "300 Beale Street", "zip_code": "38103", "phone": "(901) 555-3636", "description": "Blues city, rock-bottom prices.", "lat": "35.1495", "long": "-90.0490"},
    {"name": "Charlotte Auto World", "city": "Charlotte", "state": "North Carolina", "address": "400 Trade St", "zip_code": "28202", "phone": "(704) 555-3737", "description": "Queen City's car castle.", "lat": "35.2271", "long": "-80.8431"},
    {"name": "Raleigh Car Center", "city": "Raleigh", "state": "North Carolina", "address": "100 Fayetteville St", "zip_code": "27601", "phone": "(919) 555-3838", "description": "Triangle's top dealer.", "lat": "35.7796", "long": "-78.6382"},
    {"name": "Columbus Auto Sales", "city": "Columbus", "state": "Ohio", "address": "500 High Street", "zip_code": "43215", "phone": "(614) 555-3939", "description": "Ohio capital's car connection.", "lat": "39.9612", "long": "-82.9988"},
    {"name": "Cleveland Motors", "city": "Cleveland", "state": "Ohio", "address": "600 Euclid Ave", "zip_code": "44114", "phone": "(216) 555-4040", "description": "Forest City's finest dealer.", "lat": "41.4993", "long": "-81.6944"},
    {"name": "Cincinnati Auto Hub", "city": "Cincinnati", "state": "Ohio", "address": "700 Vine St", "zip_code": "45202", "phone": "(513) 555-4141", "description": "Queen of the West's car quest.", "lat": "39.1031", "long": "-84.5120"},
    {"name": "Detroit Auto Capital", "city": "Detroit", "state": "Michigan", "address": "1 Woodward Ave", "zip_code": "48226", "phone": "(313) 555-4242", "description": "Motor City's motor dealer.", "lat": "42.3314", "long": "-83.0458"},
    {"name": "Grand Rapids Motors", "city": "Grand Rapids", "state": "Michigan", "address": "200 Monroe Ave", "zip_code": "49503", "phone": "(616) 555-4343", "description": "Furniture City's car furniture.", "lat": "42.9634", "long": "-85.6681"},
    {"name": "Indianapolis Speed Motors", "city": "Indianapolis", "state": "Indiana", "address": "1 Capitol Ave", "zip_code": "46204", "phone": "(317) 555-4444", "description": "Racing capital's racing deals.", "lat": "39.7684", "long": "-86.1581"},
    {"name": "Fort Wayne Auto Mart", "city": "Fort Wayne", "state": "Indiana", "address": "300 Main St", "zip_code": "46802", "phone": "(260) 555-4545", "description": "Summit City's car summit.", "lat": "41.0793", "long": "-85.1394"},
    {"name": "Madison Auto Gallery", "city": "Madison", "state": "Wisconsin", "address": "100 State St", "zip_code": "53703", "phone": "(608) 555-4646", "description": "Cheese state's car deals.", "lat": "43.0731", "long": "-89.4012"},
    {"name": "Milwaukee Motors", "city": "Milwaukee", "state": "Wisconsin", "address": "400 Water St", "zip_code": "53202", "phone": "(414) 555-4747", "description": "Brew City's car brew.", "lat": "43.0389", "long": "-87.9065"},
]

result = db.dealers.insert_many(dealers)
print(f"Inserted {len(result.inserted_ids)} dealers")

# Get inserted dealer IDs
dealer_ids = [str(did) for did in result.inserted_ids]

# Reviews with new fields
reviews = [
    {"dealer_id": dealer_ids[0], "name": "John D.", "review": "Great experience! The staff was very helpful and professional.", "sentiment": "positive", "purchase": "Yes", "purchase_date": "2025-06-15", "car_make": "Toyota", "car_model": "Camry", "car_year": 2025, "user": "john_doe"},
    {"dealer_id": dealer_ids[0], "name": "Test User", "review": "Fantastic services", "sentiment": "positive", "purchase": "Yes", "purchase_date": "2025-07-20", "car_make": "Honda", "car_model": "Civic", "car_year": 2025, "user": "testuser"},
    {"dealer_id": dealer_ids[1], "name": "Maria Garcia", "review": "Good selection but prices are a bit high.", "sentiment": "positive", "purchase": "No", "purchase_date": "", "car_make": "", "car_model": "", "car_year": "", "user": "maria_g"},
    {"dealer_id": dealer_ids[4], "name": "Robert Smith", "review": "Excellent customer service! Will come back.", "sentiment": "positive", "purchase": "Yes", "purchase_date": "2025-08-01", "car_make": "Ford", "car_model": "Mustang", "car_year": 2025, "user": "robert_s"},
    {"dealer_id": dealer_ids[8], "name": "Sarah Johnson", "review": "Terrible experience. The car broke down after one week.", "sentiment": "negative", "purchase": "Yes", "purchase_date": "2025-05-10", "car_make": "BMW", "car_model": "3 Series", "car_year": 2024, "user": "sarah_j"},
    {"dealer_id": dealer_ids[12], "name": "Michael Brown", "review": "Amazing deals! Saved thousands on my new truck.", "sentiment": "positive", "purchase": "Yes", "purchase_date": "2025-09-01", "car_make": "Ford", "car_model": "F-150", "car_year": 2025, "user": "michael_b"},
    {"dealer_id": dealer_ids[16], "name": "Jennifer Lee", "review": "Friendly staff and great prices!", "sentiment": "positive", "purchase": "Yes", "purchase_date": "2025-04-15", "car_make": "Toyota", "car_model": "Corolla", "car_year": 2025, "user": "jennifer_l"},
]

result = db.reviews.insert_many(reviews)
print(f"Inserted {len(result.inserted_ids)} reviews")
print(f"First dealer ID: {dealer_ids[0]}")
print("Done!")