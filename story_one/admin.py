from django.contrib import admin
from .models import Schedule, Events, EventsParticipants

admin.site.register(Schedule)
admin.site.register(Events)
admin.site.register(EventsParticipants)
# Register your models here.
