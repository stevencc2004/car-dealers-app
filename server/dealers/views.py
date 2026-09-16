from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .mongo import get_dealers_collection, get_reviews_collection, get_cars_collection
from .serializers import DealerSerializer, ReviewSerializer, CarBrandSerializer, CarModelSerializer
from bson import ObjectId

def serialize_doc(doc):
    if doc:
        import copy
        serialized = copy.deepcopy(doc)
        serialized['_id'] = str(serialized['_id'])
        return serialized
    return None

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful', 'username': user.username})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logout successful'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers(request):
    collection = get_dealers_collection()
    dealers = list(collection.find())
    serialized = [serialize_doc(d) for d in dealers]
    return Response(serialized)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request, dealer_id):
    collection = get_dealers_collection()
    try:
        dealer = collection.find_one({'_id': ObjectId(dealer_id)})
    except:
        dealer = collection.find_one({'_id': dealer_id})
    if dealer:
        return Response(serialize_doc(dealer))
    return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers_by_state(request, state):
    collection = get_dealers_collection()
    dealers = list(collection.find({'state': state}))
    serialized = [serialize_doc(d) for d in dealers]
    return Response(serialized)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_reviews(request, dealer_id):
    collection = get_reviews_collection()
    reviews = list(collection.find({'dealer_id': dealer_id}))
    serialized = [serialize_doc(r) for r in reviews]
    return Response(serialized)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_review(request):
    collection = get_reviews_collection()
    review_data = {
        'dealer_id': request.data.get('dealer_id'),
        'name': request.data.get('name'),
        'review': request.data.get('review'),
        'sentiment': analyze_sentiment(request.data.get('review', '')),
        'user': request.data.get('user', 'anonymous')
    }
    result = collection.insert_one(review_data)
    review_data['_id'] = str(result.inserted_id)
    return Response(review_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_brands(request):
    collection = get_cars_collection()
    brands = list(collection.distinct('brand'))
    return Response({'brands': brands})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_models(request):
    collection = get_cars_collection()
    cars = list(collection.find())
    serialized = [serialize_doc(c) for c in cars]
    return Response(serialized)

@api_view(['GET'])
@permission_classes([AllowAny])
def analyze_review(request):
    text = request.query_params.get('text', '')
    sentiment = analyze_sentiment(text)
    return Response({'text': text, 'sentiment': sentiment})

def dealer_detail_page(request, dealer_id):
    from django.shortcuts import render
    return render(request, 'dealer.html', {'dealer_id': dealer_id})

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