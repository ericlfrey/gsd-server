from django.db import models
# from django.contrib.auth.models import User


class Client(models.Model):

    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        '''Custom Property to combine First and Last Name'''
        return f'{self.first_name} {self.last_name}'
