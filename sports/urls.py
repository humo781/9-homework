from django.urls import path
from . import views

app_name = 'sports'
urlpatterns = [
    path('list/', views.sports_list, name='list'),
    path('detail/<int:pk>/', views.sport_detail, name='detail'),
    path('create/', views.sport_create, name='create'),
    path('update/<int:pk>/', views.sport_update, name='update'),
    path('delete/<int:pk>/', views.sport_delete, name='delete'),
]
