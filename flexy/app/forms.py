from app.models import *
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
