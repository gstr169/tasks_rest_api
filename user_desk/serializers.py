from rest_framework import serializers
from user_desk.models import User, Task


# Serializer for Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'full_name',
                  'position',
                  )


# Serializer for Tasks
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


# Serializer for Tasks on /users/<id>/tasks page
class TaskWithRelationsSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        depth = 1
