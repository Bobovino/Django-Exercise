from django.db import models
from datetime import date

class Todo(models.Model):
    title=models.CharField(max_length=100, blank=False, null=False)
    notes=models.TextField(null=True, blank=True)
    date=models.DateField(default=date.today)
    estimated_end=models.DateField(null=True, blank=True)
    priority=models.IntegerField(default=3)

    def __str__(self):
        return self.title