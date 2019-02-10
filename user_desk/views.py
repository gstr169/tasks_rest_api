from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from user_desk.models import User, Task
from user_desk.serializers import UserSerializer, TaskSerializer, TaskWithRelationsSerializer


# View for Users lists
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Allow filtering by position
    def get_queryset(self):
        users = User.objects.all()
        position = self.request.query_params.get('position', None)
        if position is not None:
            users = users.filter(position=position)
        return users


# View for Users instance
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# View for Tasks lists
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Allow filtering by name
    def get_queryset(self):
        tasks = Task.objects.all()
        task_name = self.request.query_params.get('task_name', None)
        if task_name is not None:
            tasks = tasks.filter(task_name=task_name)
        return tasks


# View for Task instance
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


# Another way to create class-based view, without generics
class TaskExecutorsList(APIView):
    """
    List all user on that task.
    """

    def get(self, request, pk, format=None):
        users = User.objects.all().filter(tasks_set=pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
