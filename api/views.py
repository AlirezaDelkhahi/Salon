from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from salon.models import *


@api_view(['GET'])
def Weekends(request):
    day = Days.objects.filter(is_weekend=True)
    serializer = DaysSerializer(day, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Agents(request):
    agents = Agent.objects.all()
    serializer =  AgentsSerializer(agents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Services(request):
    services = Service.objects.all()
    serializer = ServicesSerializer(services, many=True)
    return Response(serializer.data)