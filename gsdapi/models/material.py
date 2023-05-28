from django.db import models


class Material(models.Model):

    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='materials'
    )
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name='materials'
    )
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    acquired = models.BooleanField(default=False)
