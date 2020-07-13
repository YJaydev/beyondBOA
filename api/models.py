from django.db import models

class Task(models.Model):
    row = models.BigIntegerField
    col  = models.BigIntegerField
    value = models.CharField(max_length=800)

    def __str__(self):
        return self.row
