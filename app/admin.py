from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.Suggestion)
admin.site.register(models.TimeSlot)
admin.site.register(models.Appointment)

