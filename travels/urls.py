from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('list/', views.travels_list, name='list'),
    path('detail/<int:pk>/', views.travel_detail, name='detail'),
    path('create/', views.travel_create, name='create'),
    path('update/<int:pk>/', views.travel_update, name='update'),
    path('delete/<int:pk>/', views.travel_delete, name='delete'),
]
