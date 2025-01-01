from django.urls import path
from . import views

from .views import create_person 
from .views import add_business 


urlpatterns = [
    #path('user/', views.user_details_view, name='user_details'),
    path('upcoming_programs/', views.upcoming_programs, name='upcoming_programs'),   
    
    path('success/', views.success_view, name='success'),
    path('group/', views.group_details_view, name='group_details'),
    path('data_protection_statement/', views.data_protection_statement, name='data_protection_statement'),
    path('successbiz/', views.successbiz, name='successbiz'),
    path('sports_details_view/', views.sports_details_view, name='sports_details_view'),

    path('', views.home_view, name='home'),
    path('user/', create_person, name='create_person'), 
    path('add_business/<int:pk>/', add_business, name='add_business'), 
    path('add_business/success/', views.success, name='add_businesssuccess'),  # Add this line for the success URL
    path('success/', views.success, name='success'), 

]

