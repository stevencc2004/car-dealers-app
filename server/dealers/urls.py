from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('dealers/', views.get_dealers, name='get_dealers'),
    path('dealers/state/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('dealers/<str:dealer_id>/', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('reviews/<str:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('reviews/', views.add_review, name='add_review'),
    path('cars/brands/', views.get_car_brands, name='get_car_brands'),
    path('cars/models/', views.get_car_models, name='get_car_models'),
    path('analyze/', views.analyze_review, name='analyze_review'),
]