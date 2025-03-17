from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.create_project, name='create_project'),
    path('projects/<int:project_pk>/tasks/new/', views.create_task, name='create_task'),
    path('team-members/', views.team_member_list, name='team_member_list'),
    path('team-members/new/', views.create_team_member, name='create_team_member'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/delete/', views.delete_task, name='delete_task'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/edit/', views.edit_task, name='edit_task'),


]
