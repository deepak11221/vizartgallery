from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/profile/', views.add_profile, name='add_profile'),
    path('profile/<int:id>/', views.view_profile, name='profile'),
    path('profile/<int:id>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:id>/delete/', views.delete_profile, name='delete_profile'),
    
]