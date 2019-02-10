from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from user_desk.models import User, Task
from user_desk.serializers import UserSerializer, TaskSerializer, TaskWithRelationsSerializer
from django.shortcuts import render


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        position = self.request.query_params.get('position', None)
        if position is not None:
            users = users.filter(position=position)
        return users


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        tasks = Task.objects.all()
        task_name = self.request.query_params.get('task_name', None)
        if task_name is not None:
            tasks = tasks.filter(task_name=task_name)
        return tasks


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTaskList(generics.ListAPIView):
    serializer_class = TaskWithRelationsSerializer
    """
    List all tasks, for one user.
    """

    def get_queryset(self):
        pk = self.kwargs['pk']
        tasks = Task.objects.all().filter(executor=pk)
        return tasks


class TaskExecutorsList(APIView):
    """
    List all user on that task.
    """

    def get(self, request, pk, format=None):
        users = User.objects.all().filter(tasks_set=pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
