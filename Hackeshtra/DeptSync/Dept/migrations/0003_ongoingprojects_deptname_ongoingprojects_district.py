# Generated by Django 5.1.1 on 2024-10-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0002_resourcerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoingprojects',
            name='DeptName',
            field=models.CharField(default='Untitled Project', max_length=100),
        ),
        migrations.AddField(
            model_name='ongoingprojects',
            name='District',
            field=models.CharField(default='Untitled Project', max_length=100),
        ),
    ]
