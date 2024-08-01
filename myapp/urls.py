from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('Projects/projects/', views.projects, name="projects"),
    path('Tasks/tasks/', views.tasks, name="tasks"),
    path('tasks2/<str:title>', views.tasks2),
    path('Tasks/create_task/', views.create_task, name="create_task"),
    path('Projects/create_project/', views.create_project, name="create_project"),
    path('Projects/projects/<int:id>', views.project_detail, name="project_detail")
]
