from django.db import models
from .project import Project
from .task import Task


class Material(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    acquired = models.BooleanField(default=False)
