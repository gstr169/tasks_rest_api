from django.urls import include, path
from user_desk import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/tasks', views.UserTaskList.as_view(), name='user-tasks'),
    path('tasks/', views.TaskList.as_view(), name='tasks-list'),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('tasks/<int:pk>/users', views.TaskExecutorsList.as_view(), name='task-executors'),
]
