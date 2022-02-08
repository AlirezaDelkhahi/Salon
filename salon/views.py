from django.shortcuts import render, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import test, ReservationForm
pages = ['reservation', 'login', 'register']

class Reservation(View):
    def get(self, request):
        reservationForm = ReservationForm()
        context = {
            'pages': pages,
            'current_page': 'reservation',
            'form' : reservationForm
        }
        return render(request, 'reservation.html', context=context)
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                service = Service.objects.get(id=form.cleaned_data['service'])
                agent = Agent.objects.get(id=form.cleaned_data['agents'])
                child_count = form.cleaned_data['child_count']
                adult_count = form.cleaned_data['adult_count']
                reservedDate = form.cleaned_data['date']
                reservedTime = form.cleaned_data['time_durations']
                
                customer = request.user.customer
                new_booking = Booking.objects.create(service=service, child=child_count, adult=adult_count, agent=agent, customer=customer, reservedDate=reservedDate, reservedTime=reservedTime)
                return HttpResponse(f'ok/ final_price: {new_booking.final_price}')
            else:
                return HttpResponse('Login First!')

        