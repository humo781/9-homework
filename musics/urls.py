from django.urls import path
from . import views

app_name = 'musics'
urlpatterns = [
    path('list/', views.musics_list, name='list'),
    path('detail/<int:pk>/', views.music_detail, name='detail'),
    path('create/', views.music_create, name='create'),
    path('update/<int:pk>/', views.music_update, name='update'),
    path('delete/<int:pk>/', views.music_delete, name='delete'),
]
