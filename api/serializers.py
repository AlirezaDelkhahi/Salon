from rest_framework import serializers
from salon.models import Days, Agent, Booking, Service

class DaysSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    class Meta:
        model = Days
        fields = '__all__'
        

class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    time_durations = serializers.ReadOnlyField()
    class Meta:
        model = Service
        fields = '__all__'
        