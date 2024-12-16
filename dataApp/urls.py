from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_details_view, name='user_details'),
    path('home_view_upcoming_programs/', views.home_view_upcoming_programs, name='home_view_upcoming_programs'),

    
    
    path('success/', views.success_view, name='success'),
    path('group/', views.group_details_view, name='group_details'),
    path('data_protection_statement/', views.data_protection_statement, name='data_protection_statement'),
    path('image_slider/', views.image_slider, name='image_slider'),

    path('', views.home_view, name='home'),

]

