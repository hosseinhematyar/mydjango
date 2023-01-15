from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    # str:pk or int:pk or slug:pk is Primary Key

]
