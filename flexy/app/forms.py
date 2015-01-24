from app.models import *
from django import forms

class RegistrationForm(forms.ModelForm):

	class Meta:
		# Set this form to use the model
		model = Registration
		