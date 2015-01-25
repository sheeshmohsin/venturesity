from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
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
    url(r'^search/$', 'app.views.search'),
    url(r'^patient_list/$', 'app.views.patient_list'),
    url(r'^patient_detail/(?P<pk>[\w\-_]+)/$', 'app.views.patient_detail'),
    url(r'^save_disease/(?P<pk>\w+)/$', 'app.views.save_disease'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
