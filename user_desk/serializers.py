from rest_framework import serializers
from user_desk.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'full_name',
                  'position',
                  )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'task_name',
                  'description',
                  'created',
                  'verifier',
                  'executor',
                  )


class TaskWithRelationsSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        depth = 1