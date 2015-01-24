from django.shortcuts import render_to_response
from app.models import *
from app.forms import *
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib import messages
from django.views.generic import ListView
# Create your views here.

def home(request):
    return render_to_response('home.html')

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
        else:
            messages.error(request, "Some Error Occured")
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        return render_to_response('register.html', {'form':RegistrationForm}, context_instance=RequestContext(request))

class PatientListView(ListView):
    model = Registration
    template_name='patient_list'
