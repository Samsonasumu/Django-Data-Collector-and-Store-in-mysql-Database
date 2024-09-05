from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_details_view, name='user_details'),
    path('success/', views.success_view, name='success'),
    path('group/', views.group_details_view, name='group_details'),
    path('', views.home_view, name='home'),

]

