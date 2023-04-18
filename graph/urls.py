from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('add/graph/', views.add_graph, name='add_graph'),
    path ('graph/<int:id>/', views.view_graph, name='graph'),
    path ('graph/<int:id>/edit/', views.edit_graph, name='edit_graph'), 
    path ('graph/<int:id>/delete/', views.delete_graph, name='delete_graph'),
]