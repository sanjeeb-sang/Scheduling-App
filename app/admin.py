from django.contrib import admin
from app import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(models.Suggestion)
admin.site.register(models.TimeSlot)
admin.site.register(models.Appointment)
admin.site.register(models.Professor)
admin.site.register(models.ProfessorStudent)
admin.site.register(models.Student)

