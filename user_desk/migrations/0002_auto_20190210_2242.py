# Generated by Django 2.1.5 on 2019-02-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_desk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ManyToManyField(blank=True, related_name='tasks_set', to='user_desk.User'),
        ),
    ]
