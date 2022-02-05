from django.db import models
from django.utils.timezone import timedelta
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(verbose_name='Service Field', max_length=200, unique=True)
    duration = models.DurationField(verbose_name='Service Timespan', default=timedelta(hours=1), blank=True, null=True)    
    adultPrice = models.PositiveIntegerField(default=0, blank=True, null=True)
    childPrice = models.PositiveIntegerField(default=0, blank=True, null=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)    

    @property
    def time_durations(self) -> tuple: #time choices in a tuple for creating in forms
        step = int(self.duration.total_seconds()/3600)
        time_durations = (f'{x} - {x+step}' for x in range(self.start_time.hour, self.end_time.hour, step))
        time_durations = tuple([(x, x) for x in time_durations])
        return time_durations
    
    def __str__(self):
        return f'{self.name}#{self.id}'

class Agent(models.Model):
    name = models.CharField(verbose_name='Full Name', max_length=200)
    description = models.TextField(verbose_name='Description')
    profile_pic = models.FileField(upload_to='agent images/', verbose_name='Agent Picture', blank=True, null=True, default=None)
    service_reach = models.PositiveIntegerField(verbose_name='Service Number Reach', default=0, blank=True, null=True )
    experience_year = models.PositiveIntegerField(verbose_name='Years Of Experience', default=0, null = True, blank = True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    @property
    def imageUrl(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url

    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.name}'

class Booking(models.Model):
    child = models.IntegerField(default=0, null=True, blank=True)
    adult = models.IntegerField(default=0, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservedDate = models.DateField()
    reservedTime = models.CharField(max_length=200, blank=True, null=True)# (15 - 17) , (11 - 1)
    final_price = models.IntegerField(default=0, null=True, blank=True)
    
    @property
    def final_price(self):
        final_price = (self.child * self.service.childPrice) + (self.adult * self.service.adultPrice)
        return final_price
    
    def __str__(self):
        return f'#{self.id} - {self.service} - {self.final_price}'


class Days(models.Model):
    days = (
        (6,'شنبه'),
        (0,'یکشنبه'),
        (1,'دوشنبه'),
        (2,'سه شنبه'),
        (3,'چهارشنبه'),
        (4,'پنجشنبه'),
        (5,'جمعه'),
    )
    day = models.IntegerField(unique=True, choices=days) 
    is_weekend = models.BooleanField(default=False, null=True, blank=True) # true == holiday
    
    @property
    def title(self):
        title = [i[1] for i in self.days if i[0] == self.day]
        return title[0]

    def __str__(self):
        if self.is_weekend:
            return f'{self.title} - (holiday)'
        return f'{self.title}'

