from django.db import models
from .project import Project


class Task(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=155)
    date_created = models.DateField()
    due_date = models.DateField()
    status = models.IntegerField()
