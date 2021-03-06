from app.models import Registration, Disease
from django import forms

class RegistrationForm(forms.ModelForm):

    class Meta:
        # Set this form to use the model
        model = Registration

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': 'form-control'
                    })

class DiseaseForm(forms.ModelForm):

    class Meta:
        # Set this form to use the model
        model = Disease

        exclude=('patient',)

    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': 'form-control'
                    })
