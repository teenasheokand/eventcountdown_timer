from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
