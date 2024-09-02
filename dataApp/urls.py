from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_details_view, name='user_details'),
    path('success/', views.success_view, name='success'),

]