from django.urls import path
from . import views

urlpatterns = [
    path('djangoapp/login', views.login_user, name='login'),
    path('djangoapp/logout', views.logout_user, name='logout'),
    path('djangoapp/register', views.register_user, name='register'),
    path('djangoapp/get_cars', views.get_cars, name='get_cars'),
    path('fetchDealers', views.get_dealers, name='get_dealers'),
    path('fetchDealer/<str:dealer_id>', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('fetchDealers/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('fetchReviews/dealer/<str:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('addReview', views.add_review, name='add_review'),
    path('getCarMakes', views.get_car_brands, name='get_car_brands'),
    path('getCarModels', views.get_car_models, name='get_car_models'),
    path('analyze/<str:text>', views.analyze_review, name='analyze_review'),
]