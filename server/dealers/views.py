from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .mongo import get_dealers_collection, get_reviews_collection, get_cars_collection
from bson import ObjectId
import urllib.parse


def serialize_doc(doc):
    if doc:
        import copy
        serialized = copy.deepcopy(doc)
        serialized['id'] = str(serialized.pop('_id', ''))
        return serialized
    return None


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    userName = request.data.get('userName', request.data.get('username', ''))
    password = request.data.get('password', '')
    user = authenticate(request, username=userName, password=password)
    if user is not None:
        login(request, user)
        return Response({'userName': user.username, 'status': 'Authenticated'})
    return Response({'userName': '', 'status': 'Not Authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def logout_user(request):
    logout(request)
    return Response({'userName': ''})


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    userName = request.data.get('userName', request.data.get('username', ''))
    firstName = request.data.get('firstName', request.data.get('first_name', ''))
    lastName = request.data.get('lastName', request.data.get('last_name', ''))
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    if User.objects.filter(username=userName).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=userName, email=email, password=password, first_name=firstName, last_name=lastName)
    return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers(request):
    collection = get_dealers_collection()
    dealers = list(collection.find())
    result = []
    for d in dealers:
        result.append({
            'id': str(d['_id']),
            'full_name': d.get('name', ''),
            'short_name': d.get('name', '').split()[0] if d.get('name') else '',
            'city': d.get('city', ''),
            'state': d.get('state', ''),
            'address': d.get('address', ''),
            'zip': d.get('zip_code', ''),
            'lat': d.get('lat', '39.0997'),
            'long': d.get('long', '-94.5786'),
        })
    return Response(result)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request, dealer_id):
    collection = get_dealers_collection()
    try:
        dealer = collection.find_one({'_id': ObjectId(dealer_id)})
    except:
        dealer = collection.find_one({'_id': dealer_id})
    if dealer:
        return Response({
            'id': str(dealer['_id']),
            'full_name': dealer.get('name', ''),
            'short_name': dealer.get('name', '').split()[0] if dealer.get('name') else '',
            'city': dealer.get('city', ''),
            'state': dealer.get('state', ''),
            'address': dealer.get('address', ''),
            'zip': dealer.get('zip_code', ''),
            'phone': dealer.get('phone', ''),
            'description': dealer.get('description', ''),
            'lat': dealer.get('lat', '39.0997'),
            'long': dealer.get('long', '-94.5786'),
        })
    return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers_by_state(request, state):
    collection = get_dealers_collection()
    dealers = list(collection.find({'state': state}))
    result = []
    for d in dealers:
        result.append({
            'id': str(d['_id']),
            'full_name': d.get('name', ''),
            'short_name': d.get('name', '').split()[0] if d.get('name') else '',
            'city': d.get('city', ''),
            'state': d.get('state', ''),
            'address': d.get('address', ''),
            'zip': d.get('zip_code', ''),
            'lat': d.get('lat', '39.0997'),
            'long': d.get('long', '-94.5786'),
        })
    return Response(result)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_reviews(request, dealer_id):
    collection = get_reviews_collection()
    reviews = list(collection.find({'dealer_id': dealer_id}))
    result = []
    for r in reviews:
        result.append({
            'id': str(r['_id']),
            'dealer_id': r.get('dealer_id', ''),
            'name': r.get('name', ''),
            'review': r.get('review', ''),
            'sentiment': r.get('sentiment', 'neutral'),
            'purchase': r.get('purchase', ''),
            'purchase_date': r.get('purchase_date', ''),
            'car_make': r.get('car_make', ''),
            'car_model': r.get('car_model', ''),
            'car_year': r.get('car_year', ''),
            'user': r.get('user', ''),
        })
    return Response(result)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def add_review(request):
    collection = get_reviews_collection()
    review_data = {
        'dealer_id': request.data.get('dealer_id', ''),
        'name': request.data.get('name', ''),
        'review': request.data.get('review', ''),
        'sentiment': analyze_sentiment(request.data.get('review', '')),
        'purchase': request.data.get('purchase', ''),
        'purchase_date': request.data.get('purchase_date', ''),
        'car_make': request.data.get('car_make', ''),
        'car_model': request.data.get('car_model', ''),
        'car_year': request.data.get('car_year', ''),
        'user': request.data.get('user', 'anonymous'),
    }
    result = collection.insert_one(review_data)
    review_data['id'] = str(result.inserted_id)
    return Response(review_data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_brands(request):
    collection = get_cars_collection()
    brands = list(collection.distinct('brand'))
    return Response({'car_makes': brands})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_models(request):
    collection = get_cars_collection()
    cars = list(collection.find())
    result = []
    for c in cars:
        result.append({
            'id': str(c['_id']),
            'car_make': c.get('brand', ''),
            'car_model': c.get('model', ''),
            'car_year': c.get('year', 2024),
        })
    return Response({'car_models': result})


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def get_cars(request):
    collection = get_cars_collection()
    cars = list(collection.find())
    car_models = []
    for c in cars:
        car_models.append({
            'CarMake': c.get('brand', ''),
            'CarModel': c.get('model', ''),
        })
    return Response({'CarModels': car_models})


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def analyze_review(request, text=''):
    if not text:
        text = request.query_params.get('text', '')
    decoded_text = urllib.parse.unquote(text)
    sentiment = analyze_sentiment(decoded_text)
    return Response({'text': decoded_text, 'sentiment': sentiment})


def dealer_detail_page(request, dealer_id):
    from django.shortcuts import render
    return render(request, 'dealer.html', {'dealer_id': dealer_id})


def review_page(request, dealer_id):
    from django.shortcuts import render
    username = request.user.username if request.user.is_authenticated else 'anonymous'
    return render(request, 'review.html', {'dealer_id': dealer_id, 'username': username})


def analyze_sentiment(text):
    positive_words = ['great', 'excellent', 'good', 'fantastic', 'wonderful', 'amazing', 'love', 'best', 'happy', 'satisfied']
    negative_words = ['bad', 'terrible', 'poor', 'awful', 'worst', 'hate', 'horrible', 'disappointed', 'angry', 'unhappy']

    text_lower = text.lower()
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)

    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    return 'neutral'