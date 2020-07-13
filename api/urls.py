from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name = "api-overview"),
    path('task-list/', views.taskList, name="tak-list"),
    path('task-details/<str:pk>', views.taskDetails, name = "task-details"),
    path('task-create/', views.taskCreate, name="tak-Create"),
    path('task-update/', views.taskUpdate, name="tak-Update"),
    path('data-update/<str:pk>', views.dataUpdate, name = "data-update"),
    path('data-update1/', views.dataUpdate1, name = "data-update")
]