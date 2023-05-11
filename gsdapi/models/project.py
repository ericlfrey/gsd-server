from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional address field to capture from the client
    title = models.CharField(max_length=155)
    date_created = models.DateField()

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
