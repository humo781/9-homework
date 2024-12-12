from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('list/', views.movies_list, name='list'),
    path('detail/<int:pk>/', views.movie_detail, name='detail'),
    path('create/', views.movie_create, name='create'),
    path('update/<int:pk>/', views.movie_update, name='update'),
    path('delete/<int:pk>/', views.movie_delete, name='delete'),
]
