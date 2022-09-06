from django.db import models

# Create your models here.
class Schedule(models.Model):
    subject = models.CharField(max_length = 50)
    lecturer = models.CharField(max_length = 50)
    room = models.CharField(max_length = 50)
    credit = models.CharField(max_length = 10)
    term = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)

class Events(models.Model):
    event = models.CharField(max_length = 50)
    day = models.CharField(max_length = 10)
    date = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    def __str__ (self):
        return self.event

class EventsParticipants(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    eventName = models.ForeignKey(Events, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name