import pymongo
import datetime
from django.db import models
from djangotoolbox.fields import EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager
from django_mongodb_engine.storage import GridFSStorage
from app.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _

gridfs_storage = GridFSStorage()
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
    picture = models.ImageField(_('Patient Image'), upload_to=get_upload_file_path)
    #doctor = models.CharField(choices=DOCTOR_CHOICE, max_length=25)
    objects = MongoDBManager()

    def __unicode__(self):
        return self.first_name

class Disease(models.Model):
    patient = models.ForeignKey('Registration')
    symptom = models.CharField(_('Disease Symptom'), max_length=50)
    doctor = models.CharField(_('Doctor Consulted'), max_length=50)
    prescription = models.CharField(_('Prescription'), max_length=50)
    report = models.FileField(_('Report Attachment'), upload_to=get_upload_file_path)
    disease = models.CharField(_('Detected Disease'), max_length=50)
    cured = models.BooleanField()
    objects = MongoDBManager()

    def __unicode__(self):
        return self.disease
    
