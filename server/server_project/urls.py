from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from dealers.views import dealer_detail_page, review_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dealers.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login_page'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register_page'),
    path('dealers/<str:dealer_id>/', dealer_detail_page, name='dealer_detail'),
    path('dealers/<str:dealer_id>/review/', review_page, name='review_page'),
]