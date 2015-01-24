from django.db import models

# Create your models here.
class Registration(models.Model):
	DOCTOR_CHOICE = (
		('Mohsin', 'mohsin'),
	)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.CharField(max_length=3)
	mobile = models.CharField(max_length=12)
	date = models.CharField(max_length=25)
	doctor = models.CharField(choices=DOCTOR_CHOICE, max_length=25)