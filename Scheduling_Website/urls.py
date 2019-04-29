"""petHelperApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name = 'index'),

    url(r'^contact$', views.contact, name = 'contact'),

    url(r'^legal_information$', views.legal_information, name = 'legal_information'),

    url(r'^about$', views.about, name = 'about'), 
      
    url(r'^help/$', views.help, name = 'help'),
      
    url(r'^signup/$', views.signup, name = 'signup'),

    url('accounts/', include('django.contrib.auth.urls')),

    url(r'^profile/$', views.profile, name='profile'),

    url(r'^suggestions/$', views.suggestions, name='suggestions'),

    url(r'all_suggestions/$', views.all_suggestions, name='all_suggestions'),

    url(r'suggestions/delete/(?P<id>\d+)$', views.delete_suggestion, name='delete_suggestion'),
        
    url(r'^timeslots/$', views.timeslots, name='timeslots'),

    url(r'^all_timeslots/$', views.all_timeslots, name='all_timeslots'),
    
    url(r'timeslots/delete/(?P<id>\d+)$', views.delete_timeslot, name='delete_timeslot'),

    url(r'^appointments/$', views.appointments, name='appointments'),

    url(r'all_appointments/$', views.all_appointments, name='all_appointments'),

    url(r'appointments/delete/(?P<id>\d+)$', views.delete_appointment, name='delete_appointment'),
    
    url(r'send_remainder_emails/$', views.send_remainder_emails, name='send_remainder_emails'),

]
