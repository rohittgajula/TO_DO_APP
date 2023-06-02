from django.urls import path

from app import views

urlpatterns = [
    path('tasks/', views.TaskAPI.as_view()),
    path('tags/', views.TagAPI.as_view()),
]