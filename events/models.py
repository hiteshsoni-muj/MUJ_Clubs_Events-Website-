from django.db import models

class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    club = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.club}"