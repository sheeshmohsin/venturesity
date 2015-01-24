from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flexy.views.home', name='home'),
    # url(r'^flexy/', include('flexy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'app.views.home'),
    url(r'^register/$', 'app.views.register'),
    url(r'^patient_list/$', views.PatientListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
