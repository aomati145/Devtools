from django.contrib import admin
from .models import CaregiverProfile, ElderProfile, Appointment

# Register your models here.
admin.site.register(CaregiverProfile)
admin.site.register(ElderProfile)
admin.site.register(Appointment)
