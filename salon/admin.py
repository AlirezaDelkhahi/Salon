from django.contrib import admin
from .models import Agent, Customer, Booking, Days, Service
# Register your models here.

admin.site.register([Agent, Customer, Booking, Days, Service])