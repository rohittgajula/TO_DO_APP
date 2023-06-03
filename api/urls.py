from django.urls import path

from app import views

urlpatterns = [
    path('tasks/', views.TaskAPI.as_view()),

    # adding new tags api to add/delete tags
    path('tags/', views.TagAPI.as_view()),
]