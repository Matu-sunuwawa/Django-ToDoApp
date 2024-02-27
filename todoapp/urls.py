from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.lists, name='list'),
    path('add_lists/',views.add_list, name='add_lists'),
    path('update_lists/<str:pk>/', views.update_list, name='update_lists'),
    path('delete_list/<str:pk>/', views.delete_list, name='delete_list'),
]