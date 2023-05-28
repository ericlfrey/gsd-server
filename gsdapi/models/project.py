from django.db import models


class Project(models.Model):
    user = models.ForeignKey('Client', on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    date_created = models.DateField()
