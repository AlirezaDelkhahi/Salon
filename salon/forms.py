from django.forms import ModelForm
from .models import Booking
from django import forms
from django.forms import DateField
class test(ModelForm):
    class Meta:
        model = Booking
        fields = ['child','adult', 'service', 'reservedDate']
        widgets = {
            'reservedDate': forms.TextInput(attrs={'class': 'dateInput' , 'autocomplete':'off'})
        }
            # firstname= forms.CharField(widget= forms.TextInput
            #                (attrs={'class':'some_class',
			# 	   'id':'some_id'}))
            # autocomplete="off"

class ReservationForm(forms.Form):
    service = forms.IntegerField(label='service', widget=forms.Select(attrs={'id': 'id_service'}))
    adult_count = forms.IntegerField(label='Adult', initial=0, widget=forms.NumberInput(attrs={'min': '0'}))
    child_count = forms.IntegerField(label='Child', initial=0, widget=forms.NumberInput(attrs={'min': '0'}))
    # date = forms.CharField(label='Date : ', widget=forms.TextInput(attrs={'id':'id_date'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))
    time_durations = forms.CharField(label='times', widget=forms.Select(attrs={'id': 'id_time_duration'}))
    agents = forms.CharField(label='agent', widget=forms.Select(attrs={'id': 'id_agent'}))
