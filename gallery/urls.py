from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/category/', views.add_category, name='add_category'),
    path('add/snippet/', views.add_snippet, name='add_snippet'),
    path('category/<int:id>/', views.view_category, name='category'),
    path('snippet/<int:id>/', views.view_snippet, name='snippet'),
    path('category/<int:id>/edit/', views.edit_category, name='edit_category'),
    path('snippet/<int:id>/edit/', views.edit_snippet, name='edit_snippet'),
    path('category/<int:id>/delete/', views.delete_category, name='delete_category'),
    path('snippet/<int:id>/delete/', views.delete_snippet, name='delete_snippet'),
]