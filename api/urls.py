from django.urls import path, include
from .views import *


urlpatterns = [
    path('weekend-list/', Weekends, name='weekend-list'),
    path('agent-list/', Agents, name='agent-list'),
    path('booking-list/', Bookings, name='booking-list'),
    path('service-list/', Services, name='service-list')
]
