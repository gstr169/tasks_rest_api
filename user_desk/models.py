from django.db import models


# Create your models here.
class User(models.Model):
    full_name = models.TextField()
    position = models.TextField(blank=True)

    def __str__(self):
        return self.full_name + ' ' + self.position


class Task(models.Model):
    task_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    verifier = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='verifying_set')
    executor = models.ManyToManyField(User,
                                      blank=True,
                                      related_name='tasks_set')

    def __str__(self):
        return self.task_name
