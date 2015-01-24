import pymongo
import datetime
from django.db import models
from djangotoolbox.fields import EmbeddedModelField
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Registration(models.Model):
    DOCTOR_CHOICE = (
        ('mohsin', 'Mohsin'),
        ('sheesh', 'Sheesh'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    mobile = models.CharField(max_length=12)
    date = models.DateField(default=datetime.date.today())
    doctor = models.ForeignKey('Doctor')
    #doctor = models.CharField(choices=DOCTOR_CHOICE, max_length=25)

    def __unicode__(self):
        return self.first_name
