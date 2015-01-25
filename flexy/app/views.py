from django.shortcuts import render_to_response
from app.models import *
from app.forms import RegistrationForm, DiseaseForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import messages
from django.views.generic import ListView, DetailView
from itertools import chain
from pymongo import MongoClient
from bson.objectid import ObjectId  

client = MongoClient()
db = client.sheesh
# Create your views here.

def home(request):
    return render_to_response('home.html')

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return render_to_response('register.html', {'form':RegistrationForm}, context_instance=RequestContext(request))
        else:
            messages.error(request, "Some Error Occured")
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        return render_to_response('register.html', {'form':RegistrationForm}, context_instance=RequestContext(request))

class PatientListView(ListView):
    model = Registration
    template_name='patient_list.html'

def search(request):
    search = request.GET['q']
    collection = db.app_registration
    a_list = collection.find({"first_name":search})
    b_list = collection.find({"last_name":search})
    c_list = collection.find({"age":search})
    d_list = collection.find({"mobile":search})
    e_list = collection.find({"doctor":search})
    data = list(chain(a_list, b_list, c_list, d_list, e_list))
    return render_to_response('patient_list.html', {'object_list':data})

class PatientDetailView(DetailView):
    model = Registration
    template_name = 'patient_detail.html'

def patient_list(request):
    data = db.app_registration.find()
    return render_to_response('patient_list.html', {'object_list':data})

def patient_detail(request, pk):
    collection = db.app_registration
    oneobj = collection.find_one({"_id":ObjectId(pk)})
    diseases = db.app_disease.find({"patient":ObjectId(pk)})
    return render_to_response('patient_detail.html', {'object':oneobj, 
        'diseases':diseases, 'form':DiseaseForm, 'pk':pk},
         context_instance=RequestContext(request))

def save_disease(request, pk):
    field_list = ['csrfmiddlewaretoken']
    oneobj = db.app_registration.find_one({"_id":ObjectId(pk)})
    diseases = db.app_disease.find({"patient":ObjectId(pk)})
    finaldict = dict()
    if request.method=="POST":
        form = DiseaseForm(request.POST)
        if form.is_valid:
            for key, value in request.POST.iteritems():
                if key not in field_list:
                    finaldict[key] = value
            finaldict['patient'] = ObjectId(pk)
            db.app_disease.insert(finaldict)
            messages.success(request, "Saved Successfully")
            return HttpResponseRedirect(reverse("patient_detail", kwargs={"pk": pk}))
            return render_to_response('patient_detail.html', {'object':oneobj,
            'diseases':diseases, 'form':DiseaseForm, 'pk':pk},
            context_instance=RequestContext(request))
        else:
            messages.error(request, "Some error occured")
            return render_to_response('patient_detail.html', {'object':oneobj,
            'diseases':diseases, 'form':form, 'pk':pk},
            context_instance=RequestContext(request))
    else:
        return HttpResponse("Something fishy is going on")

